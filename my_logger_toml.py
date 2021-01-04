import logging
import logging.config

logging.config.fileConfig(fname='my_config.toml', disable_existing_loggers=False)

# Get the default fallback root logger
logger = logging.getLogger(__name__)
logger.debug('This is a debug message with a non-configured logger name. It will default to root config.')

# Get the specific configured logger
logger = logging.getLogger('sampleLogger')
logger.debug('This is a debug message with sampleLogger. See the difference?')