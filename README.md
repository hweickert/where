=====
where
=====

Locates absolute file paths like the Windows 'where' or the Linux 'which' utility.
Makes use of the PATH variable and the current directory.

## Usage

### where()
Returns all matching file paths in a list.

    >>> import where

    >>> where.where( "python" )
    ['C:\\Python27\\python.exe']


### first()
Returns first matching file path or None (if nothing found).

    >>> import where

    >>> where.first( "python" )
    'C:\\Python27\\python.exe'

    >>> where.first( "spaghetti-monster" )
    None
