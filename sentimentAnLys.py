#import csv
from textblob import *


feedback1="Interstellar is impressive. It is superbly made, and combines compelling thought about everything from ecology to the nature of time to a child's belief in ghosts into something cohesive and mostly engrossing."
feedback2="The summary work of Nolan: apotheosis of his signature where he attempts to merge the philosophical and emotional in entertaining genre packages."
feedback3="It's the rare combination of a film that's both enjoyable in the theater and afterward, hashing through it over a drink"
feedback4="Interstellar magnifies Nolan's style to a tremendous degree, but that also means enlarging his own flaws too."
feedback5="For this critic, Nolan hits shy of the mark for cinematic brilliance but still manages to land a visually stunning entertainment in its own right."
feedback6="Succeeds on a level that has been largely foreign to the celluloid-loving director: the emotional."
feedback7="The planets in the new galaxies are creatively different yet familiar, beautiful and ugly, habitable but not habitable. They have their own histories and realities and have no interest in being colonised by the US of A."
feedback8="The enchantment of a Christopher Nolan film, the sheer majesty of it, if you will, is surrendering to it."
feedback9="Interstellar is an ambitious story, and while the theme of love transcends time and space is a bit shoehorned into the script, it still rings true. Matthew McConaughey delivers one of the finest pieces of acting on film."
feedback10="I think the reason why I connected so deeply with it is the extent to which Nolan evokes iconic moments from silent films."
feedback11="What is wrong with the movie - some of the messages are lathered on so thickly... yet the Nolan brothers assume that all viewers have a keen grasp of quantum physics, relativity, time dimensions and gravity."
feedback12="The result is a mess. But it's a beautiful mess, and one that I wouldn't want you to miss for the world."
feedback13="Watching Christopher Nolan fall short is still more exciting than watching most other directors succeed."
feedback14="Nolan's refreshing love affair with self-determination goes too far."
feedback15="visually spectacular, complex, and both intellectually and emotionally stimulating...[Full review in Spanish]"
feedback16="Visually striking, with an impressive cast... [Full review in Spanish]"
feedback17="Christopher Nolan's spectacular film is filled with frustration, anger, and guilt, and also strives for acceptance and even redemption."
feedback18="Eye-popping visuals, an ambitious narrative, and a heart-racing soundtrack; one of Nolan's best"
feedback19="Interstellar is why we go to the movies."
feedback20="This intergalactic extravaganza is clearly in a class by itself."

blob1=TextBlob(feedback1)
blob2=TextBlob(feedback2)
blob3=TextBlob(feedback3)
blob4=TextBlob(feedback4)
blob5=TextBlob(feedback5)
blob6=TextBlob(feedback6)
blob7=TextBlob(feedback7)
blob8=TextBlob(feedback8)
blob9=TextBlob(feedback9)
blob10=TextBlob(feedback10)
blob11=TextBlob(feedback11)
blob12=TextBlob(feedback12)
blob13=TextBlob(feedback13)
blob14=TextBlob(feedback14)
blob15=TextBlob(feedback15)
blob16=TextBlob(feedback16)
blob17=TextBlob(feedback17)
blob18=TextBlob(feedback18)
blob19=TextBlob(feedback19)
blob20=TextBlob(feedback20)


print(blob1.sentiment)
print(blob2.sentiment)
print(blob3.sentiment)
print(blob4.sentiment)
print(blob5.sentiment)
print(blob6.sentiment)
print(blob7.sentiment)
print(blob8.sentiment)
print(blob9.sentiment)
print(blob10.sentiment)
print(blob11.sentiment)
print(blob12.sentiment)
print(blob13.sentiment)
print(blob14.sentiment)
print(blob15.sentiment)
print(blob16.sentiment)
print(blob17.sentiment)
print(blob18.sentiment)
print(blob19.sentiment)
print(blob20.sentiment)
