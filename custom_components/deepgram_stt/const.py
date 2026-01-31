"""Constants for Deepgram STT integration."""

DOMAIN = "deepgram_stt"

# API Configuration
DEFAULT_MODEL = "nova-3"
DEFAULT_LANGUAGE = "pl"
DEFAULT_ENCODING = "linear16"
DEFAULT_SAMPLE_RATE = 16000

# Streaming Configuration
STREAM_DELAY = 0.01
TRANSCRIPT_TIMEOUT = 5

# Config Keys
CONF_API_KEY = "api_key"
CONF_MODEL = "model"
CONF_LANGUAGE = "language"
