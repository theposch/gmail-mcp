# Enhanced Gmail MCP Server

A powerful and feature-rich Model Context Protocol (MCP) server for Gmail integration, written in Python. This server enables AI assistants like Claude to interact with Gmail through natural language, providing comprehensive email management capabilities.

## 🌟 Key Features

### 📧 Complete Email Management
- Send emails with customizable subject, content, and recipients
- Read and retrieve email content with full metadata
- Move emails to trash with confirmation
- Mark emails as read/unread
- Open emails directly in browser

### 📝 Draft Management
- Create draft emails for later review
- List all draft emails
- Edit existing drafts

### 🏷️ Advanced Label Management
- List all available labels
- Create custom labels
- Apply/remove labels from emails
- Rename existing labels
- Delete unused labels
- Search emails by label

### 📁 Folder Organization
- Create new folders (implemented as Gmail labels)
- Move emails between folders
- List all available folders

### 🔍 Powerful Search & Filtering
- Search emails using Gmail's advanced query syntax
- Create, manage, and delete email filters
- Filter by sender, recipient, subject, content, and more
- Customize search results with flexible parameters

### 🗄️ Archive Management
- Archive emails (remove from inbox without deleting)
- Batch archive multiple emails matching search criteria
- List all archived emails
- Restore archived emails to inbox

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Python MCP SDK >= 2.0
- Google Cloud project with Gmail API enabled
- OAuth 2.0 credentials

### Installation

```bash
# Clone the repository
git clone https://github.com/theposch/gmail-mcp.git
cd gmail-mcp

# Set up a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install the package
pip install -e .
```

### Google Cloud Setup

1. Create a [new Google Cloud project](https://console.cloud.google.com/projectcreate)
2. [Enable the Gmail API](https://console.cloud.google.com/apis/library/gmail.googleapis.com)
3. Configure the [OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent):
   - Select "External" user type
   - Add your email as a test user
   - Add the scope: `https://www.googleapis.com/auth/gmail/modify`
4. Create [OAuth 2.0 credentials](https://console.cloud.google.com/apis/credentials):
   - Choose "Desktop app" as the application type
   - Download the JSON credentials file

### Configuration

Store your credentials securely and specify their location when running the server:

```bash
# Example directory structure for credentials
mkdir -p ~/.gmail-mcp
# Move your downloaded credentials file
mv ~/Downloads/client_secret_*.json ~/.gmail-mcp/credentials.json
```

## 🔧 Usage

### Running with Claude Desktop

Add the following to your Claude Desktop configuration file (typically at `~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "gmail": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/gmail-mcp",
        "run",
        "gmail",
        "--creds-file-path",
        "/absolute/path/to/credentials.json",
        "--token-path",
        "/absolute/path/to/tokens.json"
      ]
    }
  }
}
```

### Testing with MCP Inspector

For testing and debugging, use the MCP Inspector:

```bash
npx @modelcontextprotocol/inspector uv run /path/to/gmail-mcp/src/gmail/server.py --creds-file-path /path/to/credentials.json --token-path /path/to/tokens.json
```

## 🔐 Security Considerations

- **Never commit credentials or token files to version control**
- Store credentials in a secure location with appropriate permissions
- The server will request user confirmation before performing sensitive actions
- Review Google Cloud Console regularly for unusual activity
- Consider using environment variables for sensitive paths

## 🛠️ Architecture

This implementation features a comprehensive single-file architecture that handles all Gmail operations through the Google API client libraries. Key components include:

- OAuth2 authentication with automatic token refresh
- Comprehensive error handling and logging
- Structured tool definitions with clear input schemas
- Efficient email parsing and formatting

## 📚 Example Prompts

Try these prompts with Claude after connecting the Gmail MCP server:

- "Show me my unread emails"
- "Search for emails from example@domain.com with attachments"
- "Create a new label called 'Important Projects'"
- "Draft an email to john@example.com about the upcoming meeting"
- "Archive all emails from newsletter@example.com"
- "Create a filter to automatically label emails from my team"

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the GPL-3.0 License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by various MCP server implementations in the community
- Built with the [Model Context Protocol](https://modelcontextprotocol.io/) framework
- Uses Google's official API client libraries
