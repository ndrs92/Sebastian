Sebastian
===================

Sebastian is a virtual butler to watch your door. It can show any webpage you tell him to show in a file that he's watching. Just change its contents and he'll refresh its webpage.

This software is meant to work in a private environment in which door status of whats inside is needed (know if there are workers inside etc.)

You can use this software to show if your store is opened, and to refresh live the work hours. Also it is useful to show info in a webpage that you want passersby to know.

----------

How to use
-------------

Sebastian is fairly simple. Just open `sebastian.py` with a python interpreter, select a file to watch and start sebastian. It will autorefresh whenever that file is changed.

To show Sebastian as fullscreen at startup just check the `Run on Startup` checkbox

> **Note:**
> - Sebastian needs [PySide](https://pypi.python.org/pypi/PySide/) to work. Install it with pip (pip install PySide).

How to use the sample web interface
-------------
The sample-web-interface directory is meant to be hosted in a webserver in the same computer as Sebastian is running. This way, when you want to change the contents of the Sebastian window you can access the ip/dn of your host to see the webpage. 

In Sebastian you have to set the file to watch to "site-file.txt" (inside sample-web-interface), as it'll be changing over time.

This is meant to provide a more out-of-the-box experience.

Credits
-------------
This software was developed by Andrés Vieira.
Project minds: [Andrés Vieira](https://github.com/ndrs92) & [Samuel Rodríguez](https://github.com/srborines)

License
-------------
Copyright (C) 2016  Andrés Vieira Vázquez

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
