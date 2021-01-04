import logging
import logging.config
from yaml import safe_load

with open('my_config.yaml', 'r') as f:
    config = safe_load(f.read())
    logging.config.dictConfig(config)

# Get the default fallback root logger
logger = logging.getLogger(__name__)
logger.debug('This is a debug message with a non-configured logger name. It will default to root config.')

# Get the specific configured logger
logger = logging.getLogger('sampleLogger')
logger.debug('This is a debug message with sampleLogger. See the difference?')