from . import server
import asyncio
import argparse

def main():
    """Main entry point for the package."""
    parser = argparse.ArgumentParser(description='Gmail API MCP Server')
    parser.add_argument('--creds-file-path',
                        required=True,
                        help='OAuth 2.0 credentials file path')
    parser.add_argument('--token-path',
                        required=True,
                        help='File location to store and retrieve access and refresh tokens for application')
    parser.add_argument('--port',
                        type=int,
                        default=0,
                        help='Port for local OAuth redirect server (default: 0 for dynamic port)')
    parser.add_argument('--redirect-uri',
                        default=None,
                        help='Custom redirect URI (useful for Web Application OAuth credentials)')
    parser.add_argument('--auth-only',
                        action='store_true',
                        help='Perform interactive authentication, save tokens, and exit without starting MCP server')
    
    args = parser.parse_args()
    asyncio.run(
        server.main(
            creds_file_path=args.creds_file_path,
            token_path=args.token_path,
            port=args.port,
            redirect_uri=args.redirect_uri,
            auth_only=args.auth_only,
        )
    )

# Optionally expose other important items at package level
__all__ = ['main', 'server']
