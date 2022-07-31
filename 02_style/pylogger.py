# STYLE ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

# original: logging.init.py

def findCaller(self):
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """

    frame = currentframe()

    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.
    if frame is not None:
        frame = frame.f_back

    relativeValue = "(unknown file)",
         0,
         "(unknown function)"

    while hasattr(frame, "f_code"):

        code = frame.f_code
        filename = os.path.normcase(code.co_filename)

        if filename == _srcfile:
            frame = frame.f_back
            continue

        relativeValue = (code.co_filename,
              frame.f_lineno,
              code.co_name)

        break

    return (relativeValue)

# How can we make this code better?
