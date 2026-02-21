import argparse
from quran_phonetic_search import QuranSearch

searcher = QuranSearch()

def main():
    # Setup CLI parser with subcommands
    parser = argparse.ArgumentParser(
        description="Quran Word Search CLI - fuzzy search for Arabic words from phonetic/latin input"
    )
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    query_parser = subparsers.add_parser("query", help="Search for a word")
    query_parser.add_argument(
        "query",
        type=str,
        help="The word to search for (phonetic or simple Latin)"
    )
    query_parser.add_argument(
        "--limit",
        type=int,
        default=3,
        help="Maximum number of results to return (default: 3)"
    )

    reload_parser = subparsers.add_parser("reload", help="Reload the CSV database into memory")

    args = parser.parse_args()

    if args.command == "query":
        results = searcher.query_word(args.query, limit=args.limit)
        if results:
            print(f"Top {len(results)} match(es) for '{args.query}':")
            for idx, word in enumerate(results, 1):
                print(word.strip())
        else:
            print(f"No matches found for '{args.query}'.")

    elif args.command == "reload":
        QuranSearch.load()
        print("Database reloaded successfully!")

    else:
        parser.print_help()

if __name__ == '__main__':
    main()