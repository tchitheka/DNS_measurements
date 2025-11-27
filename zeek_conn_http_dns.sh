#!/bin/bash
#
# Combine Zeek logs from multiple PCAPs using Dockerized Zeek
# Keeps only first header for each log type, removes repeated headers.
#

PCAP_DIR="."
OUTPUT_DIR="$PCAP_DIR/combined_logs"
mkdir -p "$OUTPUT_DIR"

ALL_CONN="$OUTPUT_DIR/all_conn.log"
ALL_DNS="$OUTPUT_DIR/all_dns.log"
ALL_HTTP="$OUTPUT_DIR/all_http.log"

> "$ALL_CONN"
> "$ALL_DNS"
> "$ALL_HTTP"

echo "📦 Starting Zeek processing for PCAPs in: $PCAP_DIR"
echo "-----------------------------------------------------------"

first_conn=true
first_dns=true
first_http=true

for pcap in "$PCAP_DIR"/*.pcap; do
    [ -e "$pcap" ] || { echo "No .pcap files found."; exit 1; }

    echo "▶️ Processing: $(basename "$pcap")"

    docker run --rm -v "$(pwd)":/pcaps -w /pcaps zeek/zeek \
        zeek -r "$(basename "$pcap")" >/dev/null 2>&1

    # === conn.log ===
    if [ -f conn.log ]; then
        echo "  → Merging conn.log"
        if $first_conn; then
            cat conn.log >> "$ALL_CONN"
            first_conn=false
        else
            grep -v '^#' conn.log >> "$ALL_CONN"
        fi
    fi

    # === dns.log ===
    if [ -f dns.log ]; then
        echo "  → Merging dns.log"
        if $first_dns; then
            cat dns.log >> "$ALL_DNS"
            first_dns=false
        else
            grep -v '^#' dns.log >> "$ALL_DNS"
        fi
    fi

    # === http.log ===
    if [ -f http.log ]; then
        echo "  → Merging http.log"
        if $first_http; then
            cat http.log >> "$ALL_HTTP"
            first_http=false
        else
            grep -v '^#' http.log >> "$ALL_HTTP"
        fi
    fi

    # Clean temporary Zeek logs
    rm -f *.log *.json *.bro >/dev/null 2>&1

    echo "✅ Done with: $(basename "$pcap")"
    echo "-----------------------------------------------------------"
done

echo "🎉 All PCAPs processed successfully!"
echo "Combined logs saved in: $OUTPUT_DIR"
echo "  - $ALL_CONN"
echo "  - $ALL_DNS"
echo "  - $ALL_HTTP"
