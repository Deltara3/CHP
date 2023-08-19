# CHP
Because I can, not because I should.

CHP is a CHIP-8 interpreter written in SPWN.

# Features
- Supports every opcode but input related ones.
- Faster due to RWRT.
- Actually passes all the tests.
- RND isn't implemented due to the lack of `$.random`.

# Usage
- You'll need a copy of SPWN's RWRT bytecode branch. You can get this by compiling it.
- Next you'll need a copy (or symlink) of the RWRT `libraries` folder in the folder you get from cloning this.
- Currently RWRT doesn't have anyway of reading files, you'll need to use `generate.py` to convert a ROM file into a `rom.spwn` file that CHP can use. You can do this with `python generate.py <rom path>`.
- Finally, run `main.spwn` with the `-n` option for no level.
