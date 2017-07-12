# effective-phrase-prediction

This is from the paper [effective-phrase-prediction](http://dbgroup.eecs.umich.edu/files/fcpaper07.pdf) published in VLDB 2007



# Summary of paper
### FussyTree
To train with default parameters on the tinyshakespeare corpus, run:
```bash
python train.py
```
### Significant
To sample from a trained model
```bash
python sample.py
```



# Sample output

### Restaurant Review setences
INPUT:
```
If you enjoy service by someone who is as competent as he is personable
I would recommend Corey Kaplan highly
The time he has spent here has been very productive and working with him educational and enjoyable
I hope not to need him again (though this is highly unlikely) but knowing he is there if I do is very nice
By the way
I'm not from El Centro
CA
but Scottsdale
AZ
After being on the phone with Verizon Wireless trying to figure out why my phone wasn't working for 4
5 hours
I was put in touch with Sharpie Tech
Well
after 10 seconds they fixed the problem
As the owner of a company that does our best numbers over the holiday season
having my phone out of order for 4
5 hours was horrible
Sharpie Tech fixed the problem in record time
even Verizon was shocked
I highly recommend working with this company and I look forward to working with them more
...
```


OUTPUT:
```
If you are looking 3
you are looking for 3
service was 3
by the 3
someone 5
who 6
is very 4
is a great 3
is the place 3
is not 8
is good 3
is really 5
is great 3
as a 6
as I 5
as well 4
he 15
I would 3
I was 29
I highly recommend 3
I found 3
I will 3
I didn't 4
I am 6
I go 4
I saw 3
I went 5
I decided 3
I could 6
I can 4
I had 6
I told 3
I have been 5
I got 7
I asked 3
I wanted to 3
I love 3
I don't know 4
I can't 3
I think the 3
I like 3
I understand 3
I ordered 3
would have been 3
would be 4
...
```