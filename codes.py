ntl = {
  '1':['A','B','C'],
  '2':['D','E','F'],
  '3':['G','H','I'],
  '4':['J','K','L'],
  '5':['M','N','O'],
  '6':['P','Q','R'],
  '7':['S','T','U'],
  '8':['V','W','X'],
  '9':['Y','Z']
}
ltn = {
  'A':'1','B':'1','C':'1',
  'D':'2','E':'2','F':'2',
  'G':'3','H':'3','I':'3',
  'J':'4','K':'4','L':'4',
  'M':'5','N':'5','O':'5',
  'P':'6','Q':'6','R':'6',
  'S':'7','T':'7','U':'7',
  'V':'8','W':'8','X':'8',
  'Y':'9','Z':'9',' ':' '
}

word = []
wordPs = []
counter = []

def countTheCounter():
  global counter
  global word
  x = 0
  while True:
    counter[x] += 1
    if(counter[x] >= len(word[x])):
      counter[x] = 0
      x += 1
    else:
      break


def fP(nm):
  w = open("words.txt",'r')
  words = w.read()
  words = words.split()
  global counter
  global word
  global wordPs
  word = []
  for i in str(nm):
    word.append(ntl[i])
  wordPs = []
  counter = []
  for i in word:
    counter.append(0)
  while True:
    try:
      wordPTemp = []
      for i in range(len(counter)):
        wordPTemp.append(word[i][counter[i]])
      if(''.join(wordPTemp) in words):
        wordPs.append(''.join(wordPTemp))
      countTheCounter()
    except:
      break
  if(wordPs == []):
    wordPs.append("???")
  return wordPs

def stringsToWords(st):
  st = st.split(' ')
  for i in range(len(st)):
    print(fP(st[i]))



choice = input("Would you like to...\n[1] Decode a phrase\n[2] Encode a phrase?\n> ")
if(choice == "1" or choice == "Decode" or choice == "Decode a phrase"):
  print("[>Decoder<]")
  choice = input("What sequence would you like to decode? [digits 1-9 and spaces only]\n> ")
  print("Decoding, this might take a while...")
  try:
    stringsToWords(choice)
    print("Done!")
  except:
    print("Something went wrong... did you put a charater other than 1-9 and space?")
if(choice == "2" or choice == "Encode" or choice == "Encode a phrase"):
  print("[>Encoder<]")
  choice = input("What sequence would you like to encode? [letters and spaces only]\n> ")
  print("Encoding...")
  for i in choice.upper():
    print(ltn[i],end='')
  print("\nDone!")
