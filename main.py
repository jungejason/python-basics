# main

import getopt, sys

def usage():
  print("Synopsis:")
  print("\t-v\tvalue")
  print("\t\tvalue to print out")
  print("\t-h\thelp")


def parse_args(args):
  try:
    opts, args = getopt.getopt(args, 'a:h')
  except getopt.GetoptError as err:
    print("GetoptError", err)
    usage()
    sys.exit(2)

  value = None  

  for o, a in opts:
    if o == "-h":
      usage()
      exit()
    elif o == "-a":
      value= a
    else:
      usage()
      assert False, "unhandled option"
    
  return value


def main():
  value = parse_args(sys.argv[1:])
  print("value", value)


if __name__ == "__main__":
  main()

## Output:
## 
## ~/python-basics$ python3 main.py 
## value None
## ~/python-basics$ python3 main.py -h
## Synopsis:
##     -v  value
##         value to print out
##     -h  help
## ~/python-basics$ python3 main.py -e
## GetoptError option -e not recognized
## Synopsis:
##     -v  value
##         value to print out
##     -h  help
## ~/python-basics$ python3 main.py -a vvv
## value vvv
## ~/python-basics$ python3 main.py -avvv
## value vvv
## ~/python-basics$ python3 main.py -avvv -h
## Synopsis:
##     -v  value
##         value to print out
##     -h  help
