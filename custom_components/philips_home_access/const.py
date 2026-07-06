"""Constants for the Philips Home Access integration."""
from __future__ import annotations

from datetime import timedelta

from homeassistant.const import Platform

DOMAIN = "philips_home_access"
PLATFORMS = [Platform.LOCK, Platform.BINARY_SENSOR, Platform.SENSOR]

# Config entry data keys
CONF_AREACODE = "areacode"
DEFAULT_AREACODE = "61"

# Poll intervals. Where a lock's datacenter has a realtime WebSocket, that's the
# primary update path and the poll is just a slow safety-net (also resynced on
# every WS reconnect). Datacenters without realtime (MQTT-only, not implemented)
# are poll-only, so they poll fast.
SLOW_POLL_INTERVAL = timedelta(minutes=15)
FAST_POLL_INTERVAL = timedelta(seconds=60)
