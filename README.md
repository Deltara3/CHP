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
- Currently RWRT doesn't have anyway of reading files, you'll need to use `cli.py` to convert a ROM file into a `<name>.8sp` file that CHP can use.
    - To create, use `python cli.py build <path>`. Make sure the ROM name doesn't have any special characters in it other than `_`.
    - You can switch between ROM files using `python cli.py switch <name>`, assuming the file was previously built.
    - You can list built ROM files using `python cli.py list`.
    - Or even delete them with `python cli.py delete <name>`.
    - `build` will automatically set your ROM, so there's no need to run `switch` after building.
- Finally, run `main.spwn` with the `-n` option for no level.

#### Note: CHP hides the cursor for a cleaner picture. After usage if you need to show the cursor run `python cli.py fix`.