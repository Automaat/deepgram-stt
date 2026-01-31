# Deepgram Speech-to-Text for Home Assistant

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![GitHub Release](https://img.shields.io/github/release/Automaat/deepgram-stt.svg)](https://github.com/Automaat/deepgram-stt/releases)
[![License](https://img.shields.io/github/license/Automaat/deepgram-stt.svg)](LICENSE)

Cloud-based speech-to-text integration for Home Assistant using the Deepgram API.

## Features

- **Multi-language support**: Polish, English, German, Spanish, French, Italian, Dutch, Portuguese
- **Fast and accurate**: Powered by Deepgram's Nova-3 model
- **Easy configuration**: Simple UI-based setup via Home Assistant config flow
- **Voice assistant ready**: Works seamlessly with Home Assistant voice assistants

## Installation

### HACS (Recommended)

1. Open **HACS** in Home Assistant
2. Go to **Integrations**
3. Click the three dots in the top right corner
4. Select **Custom repositories**
5. Add repository URL: `https://github.com/Automaat/deepgram-stt`
6. Category: **Integration**
7. Click **Add**
8. Search for "Deepgram Speech-to-Text"
9. Click **Download**
10. Restart Home Assistant

### Manual Installation

1. Download the latest release from [GitHub Releases](https://github.com/Automaat/deepgram-stt/releases)
2. Extract the `custom_components/deepgram_stt` directory
3. Copy to your Home Assistant `custom_components` directory
4. Restart Home Assistant

## Configuration

### Prerequisites

Get a free API key from [Deepgram Console](https://console.deepgram.com/):
1. Create an account
2. Navigate to API Keys
3. Create a new API key
4. Copy the key for use in Home Assistant

### Setup Steps

1. **Add the integration:**
   - Navigate to **Settings** > **Devices & Services**
   - Click **Add Integration**
   - Search for "Deepgram Speech-to-Text"
   - Click on it

2. **Configure:**
   - **API Key**: Paste your Deepgram API key
   - **Model** (optional): Default is `nova-3` (recommended)
   - **Language** (optional): Default is `pl` (Polish)
     - Supported: `pl`, `en`, `de`, `es`, `fr`, `it`, `nl`, `pt`

3. **Verify:**
   - Integration should appear in **Devices & Services**
   - Entity `stt.deepgram_stt` should be available in **Developer Tools** > **States**

## Using with Voice Assistants

1. Navigate to **Settings** > **Voice assistants**
2. Select your assistant (e.g., "Home Assistant")
3. Under **Speech-to-text**, select **Deepgram STT**
4. Click **Save**

Test by speaking to your voice assistant - transcription should now use Deepgram.

## Troubleshooting

### Integration doesn't appear after installation

- Ensure you restarted Home Assistant after installation
- Check logs in **Settings** > **System** > **Logs** for errors
- Verify files are in `config/custom_components/deepgram_stt/`

### API key errors

- Verify your API key is valid at [Deepgram Console](https://console.deepgram.com/)
- Check that you have API credits available
- Ensure the key wasn't regenerated or revoked

### Voice assistant not transcribing

1. Check entity state in **Developer Tools** > **States**
2. Search for `stt.deepgram_stt`
3. Verify `supported_languages` includes your configured language
4. Test with a simple voice command
5. Check Home Assistant logs for Deepgram API errors

### "Entity not found" errors

- Restart Home Assistant after changing configuration
- Verify the integration loaded successfully in **Devices & Services**

## Technical Details

- **Integration Type**: Config Flow (UI-based)
- **Platform**: STT (Speech-to-Text)
- **API**: Deepgram Live Transcription WebSocket API
- **Supported Languages**: pl, en, de, es, fr, it, nl, pt
- **Default Model**: nova-3
- **Audio Format**: WAV, PCM, 16-bit, 16kHz, mono
- **Cloud Service**: Yes (requires internet connection)

## Advanced

### NixOS Declarative Configuration

For NixOS users with declarative Home Assistant setups, you can configure the integration via config flow as normal. The integration supports standard Home Assistant configuration patterns.

## Contributing

Contributions are welcome! Please open an issue or pull request on [GitHub](https://github.com/Automaat/deepgram-stt).

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Related Documentation

- [Deepgram API Documentation](https://developers.deepgram.com/)
- [Home Assistant STT Integration](https://www.home-assistant.io/integrations/stt/)
- [Home Assistant Voice Control](https://www.home-assistant.io/voice_control/)
