# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))