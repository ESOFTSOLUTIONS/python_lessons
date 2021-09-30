mytext='X-DSPAM-Confidence:    0.8475'
posnumb=mytext.find('0.8475')
number=mytext[posnumb:]
value=float(number)
print(value)
