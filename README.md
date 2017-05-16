# Convergence-Jukebox-2
Update to the original Convergence Jukebox using a Kivy based GUI in place of Tkinter and now the working version. Convergence Jukebox 2 is a fully functional retro jukebox application. It emulates "physical" jukeboxes and is written in Python. The software has been designed to be fully functional, playing mp3's both randomly and via a credit system. More at www.convergencejukebox.com

**Convergence Jukebox 2** is open source Python based software that has been written in Python 2.7 to emulate a “retro” style jukebox. The type of jukebox that was popular in bars, restaurants and recreation areas during the 1950’s and 60’s. Written from scratch by **[Brad Fortner]** of Convergence Communications, Convergence Jukebox 2 plays properly formed ID3 tagged mp3 media. 

The Jukebox can be controlled for “personal” use by your computer keyboard but is better operated with a USB keypad. Its output resolution is modifiable allowing it to connect to inexpensive computer, laptop or TV displays with its “retro look and feel”. It can even be connected to bill, coin or card acceptors for “pay to play” situations. More information can including an **[FAQ]** and instructions on how to **[format mp3's]** be found on the Convergence Jukebox blog at **[www.convergencejukebox.com]**.

Features include;
- Unlimited mp3 library size: Currently operating in our development centre is a version containing 15,800 mp3 files. This implementation runs on minimum hardware. In this case it’s an HP MINI 210 PC that contains an Atom N450 processor, 1024 MB of memory and a ‎160.0 GB hard drive. Jukebox 2.0 has yet to be tested on a Raspberry Pi.
- Automatic Song Detection: MP3 library database is built automatically when additional properly formed ID3 tagged files are added to the media folder and the program is restarted.
- Multiple Display Resolutions: Developers can change display resolution, skins and customize all items on the screen (such as song name positions) using Pythons Kivy code.
- Customizable To Your Location: The Jukebox name or service at top of arch can be customized in the Python Kivy code.
- Background Music System: Convergence Jukebox plays library loaded in Jukebox in a continuous manner randomly. Makes an excellent background music system.
    -  Different Styles Of Music: mp3’s can be tagged with genres in comment area of ID3 tag. Random play can be set to play specific genres by altering a simple text file.
    - Songs Can Be Skipped: mp3’s can be tagged “norandom” meaning they will never play randomly. This means mp3’s with potentially unsuitable content can only be played if selected.
    - Avoids Repeating The Same Songs Continuously: mp3’s on the random list are only played once during a random play cycle.
    - Automatic Resetting Of Random List: Convergence Jukebox resets the random list when the software is rebooted or all selections in the jukebox have been played once randomly.
- Clearly Identified Songs: While song is playing, song title and artist are displayed prominently under the Jukebox arch on the display.
    - More detailed song information is displayed in the green display (top left) that includes year released, song length and album name pulled from the mp3 id3 tags.
- Convergence Jukebox plays user selected songs (paid) as a priority: When selected songs are listed in order of selection under the Upcoming Selections heading in the status area.
    - Users cannot select the same song if it’s on the Upcoming Selections list. This eliminates the same song from being played repeatedly.
    - Songs played via selection are removed from the random playlist. This eliminates the same song from being played repeatedly.
    - Random play resumes once user selected songs have completed playing.
- Number of Credits, cost per credit and the number of songs available in the library are clearly displayed (and editable in the Python code) at the bottom left of the green screen .
- Users can navigate through available music using up/down/left/right navigation keys.
- Users can navigate through music selecting songs by either Title or Artist.
- Users can navigate to the alphabetical start of either Artist or Title using specific letter keys that employ multiple keypresses.
- A log is kept of each song played randomly, each song paid to play, when the Jukebox is rebooted, when songs are added and when a new random list is generated.
- Python code has been written for is included in Convergence Jukebox that’s not been documented in the released version that talks to the Dropbox folder to providing RSS feeds for digital signage systems. As well as It is possible to include code to create tweets to Twitter accounts making the jukebox useful as a global barker system.

New In Convergence Jukebox 2.001;

- Jukebox GUI re-written in Kivy.
- Bug fix so last song on selection screen can now be accessed.
- Artists are kept in proper alphabetical order including bands that start with The.
- Bug fix so GUI wont crash when there are no titles or artists during Title Or Artist selection search.

> The Convergence Jukebox website at **[www.convergencejukebox.com]** contains links
> to Python source code.



### Version
0.001

### Tech

Convergence Jukebox uses a number of open source projects to work properly:

* **[hsaudiotag]** – sudo pip install hsaudiotag
* **[mpg321]** – sudo apt-get install mpg321
* **[pillow]** – sudo pip install pillow
* **[ImageTk]** – sudo apt-get install python-imaging-tk
* **[PyRSS2Gen]** - sudo pip installPyRSS2Gen
* **[Unclutter]** - sudo apt-get install unclutter
* **[Kivy]** - https://kivy.org/#download
* **[Keyboard]** - sudo pip install keyboard

### Installation

As soon as I figure out how to do a repository:

```sh
$ i will post code here
```

```sh
$ and here
$ and here
$ and here
$ and here
$ and here
```

### Music

Some versions of Convergence Jukebox are distributed with Creative Commons Music

* Music Distributed Under The Following Licences From http://freemusicarchive.org/
* Happy Halloween by The Vivisectors is licensed under a Attribution-NonCommercial-ShareAlike License http://creativecommons.org/licenses/by-nc-sa/4.0/
* One by Brandon Liew is licensed under a Attribution License http://creativecommons.org/licenses/by/4.0/
* Velvet Dress & Stockings by Dazie Mae is licensed under a Attribution-Noncommercial-Share Alike 3.0 United States License http://creativecommons.org/licenses/by-nc-sa/3.0/us/
* After The Last by The Red Thread is licensed under a Attribution-NonCommercial 3.0 International License http://creativecommons.org/licenses/by-nc/3.0/
* Splendid Gifts by The Willing is licensed under a Attribution-NonCommercial License http://creativecommons.org/licenses/by-nc/4.0/
* Live on WFMU with Irwin Chusid, 9/9/2015 by Barrence Whitfield and The Savages is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License http://creativecommons.org/licenses/by-nc-nd/4.0/
* Live at WFMU's Monty Hall: Oct 18, 2015 by Bridget St. John is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License http://creativecommons.org/licenses/by-nc-nd/4.0/


### Development

Want to contribute? Great! Fork the code.....

### Todos

 - So much right now I don't even want to think about it.

License
----

GNU V3 General Public License


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Brad Fortner]: <https://www.linkedin.com/in/bfortner>
   [www.convergencejukebox.com]: <http://www.convergencejukebox.com>
   [hsaudiotag]: <https://pypi.python.org/pypi/hsaudiotag>
   [mpg321]: <http://mpg321.sourceforge.net/>
   [pillow]: <https://pillow.readthedocs.org/en/3.1.x/>
   [ImageTk]: <http://pillow.readthedocs.org/en/3.0.x/reference/ImageTk.html>
   [PyRSS2Gen]: <http://www.dalkescientific.com/Python/PyRSS2Gen.html>
   [Unclutter]: <http://sourceforge.net/projects/unclutter/>
   [format mp3's]: <https://docs.google.com/document/d/1wc3l6keReNS850kQRRfQwHofUCvj3HhDXVgUWesRLf0/pub>
   [FAQ]: <https://docs.google.com/document/d/1WTYAmVawP2s8ruYispc3wRWVOO9bEDNvA2KJomWFTuw/pub>
   [Kivy]: <https://kivy.org/#home>
   [Keyboard]: <https://pypi.python.org/pypi/keyboard>
