export LD_LIBRARY_PATH="$HOME/lib/pkgconfig:$HOME/lib:$HOME/lib64:$LD_LIBRARY_PATH"

env PYTHON_CONFIGURE_OPTS="--with-system-ffi" LDFLAGS="-L $HOME/lib64/" CPPFLAGS="-I $HOME/include/"  pyenv install 3.8.11
