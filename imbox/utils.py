import logging
logger = logging.getLogger(__name__)


def str_encode(value='', encoding=None, errors='strict'):
    _encoding = 'gbk' if encoding is not None and (encoding == 'gb2312' or encoding == 'GB2312') else encoding
    logger.debug("Encode str {} with and errors {}".format(value, _encoding, errors))
    return str(value, _encoding, errors)


def str_decode(value='', encoding=None, errors='strict'):
    _encoding = 'gbk' if encoding is not None and (encoding == 'gb2312' or encoding == 'GB2312') else encoding
    if isinstance(value, str):
        return bytes(value, _encoding, errors).decode('utf-8')
    elif isinstance(value, bytes):
        return value.decode(_encoding or 'utf-8', errors=errors)
    else:
        raise TypeError("Cannot decode '{}' object".format(value.__class__))
