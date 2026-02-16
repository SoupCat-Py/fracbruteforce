# fracbruteforce
## About
goes through thousands of iteations to find equivalent fractions for any rational number (so it can repeat but not something like pi)

The TI version seems to have a really hard time checking if it found the result because it often skips right over the answer. <br/>
I've ran the same code on a computer and it does not have any trouble, so the problem seems to be with the calculator's version of python.

## Usage
### Terminal
- **Install the "humanize" module**<br/>
- Download `bruteforce.py` or clone this repo<br/>
- Run `python3 bruteforce.py -n [NUMBER] [--show-denom] [--show-all]`
  - `-n` (required) is the decimal number you want to convert to a fraction
  - `--show-denom` prints every denominator the program goes through
  - `--show-all` prints **every single iteration**<br/>I don't really recommend this as it can greatly affects performance, but it's there for debugging.

### TI-84 Plus CE Python
- Install TI Connect CE
- Download `bruteforceti.py`
- Plug in your calculator
- Drag the file into your calculator and you're done :D
