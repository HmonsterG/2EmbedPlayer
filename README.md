# 2EmbedPlayer

*A simple Python script that plays movies and TV shows using IMDb and 2embed.*
This is now deprecated due to 2embed being taken down for copyright infrigement. I'm currently working on another tool so hang tight <3

## Features
- **Simple**: Easy command-line arguments
- **Large library**: Supports a large library frequently updated by 2embed
- **Integratable**: Easily integrate into popular launchers, like Alfred

## Quick Start
Install using pip:
```
pip install IMDbPlayer
```
If you like, you may also use it by downloading and running `__main.py__`

## Usage
2EmbedPlayer works simply - you can use it with a few command-line arguments.
- `IMDbPlayer name` is used for playing movies.
- `IMDbPlayer name season episode` is used for TV shows.

## Additional Configuration
2EmbedPlayer can be integrated into Alfred on macOS. This allows easy access to playing movies and TV shows by simply searching, rather than opening a terminal.
### Prerequisites 
- As of 2023, this requires the Alfred Powerpack, which can be purchased from https://www.alfredapp.com/powerpack/
- The source of 2EmbedPlayer

### Installation
1. Create a workflow in Alfred
2. Add the keyword, e.g. `play`
3. Set `Argument Required`
4. Add `Run Script`
5. Set the contents to `python3 *location of __main__.py* '{query}'`
6. Set inputs to `with input as {query}`
7. Save and use!

This should relatively easily integrate 2EmbedPlayer into macOS, and this may be possible with other launchers -- I haven't tried others. 
