# effective-phrase-prediction

This algorithm is from the paper [effective-phrase-prediction](http://dbgroup.eecs.umich.edu/files/fcpaper07.pdf) published in VLDB 2007, Arnab Nandi, H. V. Jagadish




# Summary of paper

Here's an example of a multi-document collection. _corpus.txt_
```bash
please call me asap
please call if you
please call asap
if you call me asap
```

### Significant


![Significant](./image/definition_significant.png)



### FussyTree

![table1](./image/table1.png)

![fussytree](./image/fig1.png)





# Sample output

The data set '_yelp_academic_dataset_review.json_' is from [https://www.yelp.com/dataset_challenge](https://www.yelp.com/dataset_challenge)

### Restaurant Review setences

_yelp_academic_dataset_review.json_
````
{
    "review_id":"encrypted review id",
    "user_id":"encrypted user id",
    "business_id":"encrypted business id",
    "stars":star rating, rounded to half-stars,
    "date":"date formatted like 2009-12-19",
    "text":"review text",
    "useful":number of useful votes received,
    "funny":number of funny votes received,
    "cool": number of cool review votes received,
    "type": "review"
}
````

!e will use only _'text'_ key. To refine json file, run _read.py_
````
python read.py
````

To erase blank line, run _refine.py_
````
python refine.py
````



The refined data is in _restaurant_reviews.txt_ We only use 1000 review data.

INPUT:
```
If you enjoy service by someone who is as competent as he is personable, I would recommend Corey Kaplan highly. The time he has spent here has been very productive and working with him educational and enjoyable. I hope not to need him again (though this is highly unlikely) but knowing he is there if I do is very nice. By the way, I'm not from El Centro, CA. but Scottsdale, AZ.After being on the phone with Verizon Wireless trying to figure out why my phone wasn't working for 4.5 hours, I was put in touch with Sharpie Tech. Well, after 10 seconds they fixed the problem. As the owner of a company that does our best numbers over the holiday season, having my phone out of order for 4.5 hours was horrible. Sharpie Tech fixed the problem in record time, even Verizon was shocked. I highly recommend working with this company and I look forward to working with them more. 
-Rachel Charlupski
Founder and CEO, The Babysitting CompanyGreat service! Corey is very service oriented. Works fast and very effiecient with his time. Going to use him again real soon to do additional IT services. thanks Corey.Highly recommended. Went in yesterday looking for a dresser to use as a tv stand. Found the perfect piece for the retro look I'm going for. I found some other small decor items. Price was fair and they delivered today.  Shawn did a great job. Keep up the good work! I will definitely be back.I walked in here looking for a specific piece of furniture.  I didn't find it, but what I did find were so many things that I didn't even know I needed!  So much cool stuff here, go check it out!What a great place! Modern on Melrose has amazing furniture at great prices. I highly recommend and will be back when I am looking for new pieces.A hidden gem! Found a beautiful buffet for a great price. Whether you're looking for new or something to refurbish, this place is def worth the look!This place is a great for those vintage/mid century modern finds. From clothing to couches they have it all and great prices too.  They have similar items to their neighbors Modern Manor, but not the "designer" prices.  We got a green vintage chair for $98 and just are having the skirt around the bottom removed to show the great legs on it.  We will always check back at Melrose when looking for unique pieces for our home.This is the place to go for all your Mid Century finds.
We live in Oro Valley and it is not too far to travel when we need a specific item.
I called yesterday asking if they has something we need and minutes later I was text numerous pictures.  Because of the excellent staff, I will be going up there today.
One of my number one places to go when I go to Phoenix.
Prices are very fair for these past treasures.Great items at a good price.  Helpful, easy to deal with owners.  Just the sort of place you LIKE spending  your dollars at...and they have furniture, etc. that you don't see elsewhere.Disappointing.  I've been there twice hoping that a re-return would change my original opinion.  The first time I was there was on a Saturday, early afternoon in Spring.  I found it strange that I was the only one in the store for about 20 minutes, until another customer came in.  Melrose is usually a pretty happening place during the Spring before summer temps hit.  I saw a lot of nice 1960s furniture, mostly living room sets and home decor.  Prices were on the high end for, let's face it folks, used furniture. The blonde lady who came out to greet me after I made it to their second room (there are 3 rooms total) was frazzled and preoccupied with eating her lunch. So I went back again last week.  Didn't see the frazzled lady from before but a mid-age hipster guy at the counter who didn't have the time to greet me (sorry I disrupted your cell phone surfing).  Yep.  I was the ONLY person in the store and you obviously ignored me.  
It's just an unwelcoming place.  So much potential, but the attitude there is less than acceptable.  Will spend my $$$ elsewhere.I'm a local Real Estate agent and have fallen in love with all of the AMAZZZZZING Mid-Century Modern properties that the Phoenix and Tempe area have to offer. After listing and selling a few of these COOL homes I decided that I should be more familiar with a few MCM furniture shops that I could buy or lease a higher quality furniture. 
After going in a bunch of places I can say that I really love this store and cant wait to use them to stage my newest listing in a few months at 24th and Indian School.
Let me know if you need help finding a cool house with character to put your amazing finds from Modern on Melrose.
Enjoy
Steven
480-370-5570
stevenonmill@gmail.comModern on Melrose is one of our favorite shops on La Curva. It is on the pricey side (of an already pricey shopping experience) but I've had great success for two reasons:
First, the service has been excellent and friendly. We're new to the mcm scene and didn't get snubbed at for not being "in the know" -- sadly, this was a welcome relief. 
Second, the selection is good. Yeah, it's always a hunt, but at MOM you aren't going to be sifting through, basically, garbage to find your treasures. With most of the weeding done for you, the store is a much nicer visit.Walked into the store and stuck up a conversation with Shawn behind the counter. We talked about some furniture and other ideas I had for the home. I told him I needed a custom made shelf. Shawn asked some questions and then he sketched out a concept. I loved it. He then said Modern on Melrose has a man that does custom metal work. Three days later-it was done and it turned out better than I could have ever imagined.What a lovely place. My boyfriend and I went along with my parents (who love mid century modern furniture) just to look as I am moving soon and can't buy any furniture until I relocate, but this shop made me want to move to downtown Phoenix and fill my house with everything in this shop. My thrift-genius parents taught me to buy antique furniture and never ever ever buy new, as new furniture is expensive to buy and cheaply made. Modern on Melrose is fantastic proof of this - my boyfriend fell in love with a yellow leather and wood 70s couch and noticed that this beautiful couch cost less than a couch our friend recently bought at IKEA. And no one is going to buy IKEA couches in antique stores 40 years from now, because they barely last 1 move. 
Everything in this store is gorgeous and there is a great variety of furniture and random decor goods. We ended up buying some great stacking canisters as a gift, and the very helpful employee dashed back to the area we got them and told us they were 40% off. We debated keeping the canisters because they were as affordable as they were quirky and useful and interestingly designed, but the Christmas spirit prevailed and we decided to give them to their original recipient.
The same employee discussed style and furniture things with my father in a very helpful and absolutely non pretentious way, which is a refreshing and fun element of any antique store. I always want to talk to the employees but very often feel they are too busy or want to sound smarter than me (which they are, but I'm not buying anything if the person I'm giving money to makes me feel stupid). I was very struck by how open and helpful the employee was. Great experience. Great selection. Great prices.Unfortunately, Yelp does not allow negative stars. I was very much looking forward to going to Modern on Melrose as my sister had raved about the selection and several purchases she recently made here. I was all set to help her select more furniture for her new home until I experienced a combination of disbelief, shock and horror. 
I was inside the store when I heard a man loudly say "If you're going to start a sale, finish it!" It took a few more seconds of loud voices before I realized an argument was taking place between two employees and not two customers, as I initially thought. The male and female employee continued to loudly argue, back and forth. Feeling very uncomfortable, I started to look for my sister. There were about four other customers and we all ended up outside as we all felt very uncomfortable in the store. 
As I was walking out of the store to go out back, I heard the male employee say, in a tone that was beyond anger but instead violent, "Don't you ever tell me to shut up! Ever!" Shortly after, he walked past all 5 female customers, who had gathered out back, turned to us and angrily said "Bitch!" Not knowing what he was going to do when he returned, we decided to leave as we did not feel safe. 
It is one thing to feel uncomfortable, it is completely unacceptable to not feel safe. The interaction between the two employees was the most unprofessional thing I have ever witnessed. The male and female employee were so caught up in their own negative interaction, neither of them offered any customer service. And after their argument ended, the female employee offered no apologies and still no customer service. 
...
```


OUTPUT:
```
If you are looking for 4
If you want 5
If you have 3
If you're 4
If I 3
you don't 4
you need to 5
you are looking for 5
you are a 5
you are in 5
you have to 5
you get 7
you want a 3
you want to 5
you can get 3
you like 3
you do 3
you would 3
you should 3
you will 4
you know 3
you can't 3
you just 3
you in 6
you go 3
enjoy 10
service at 3
service was good 3
service is 12
service and 9
by this 3
by the name 3
by a 6
by another 3
someone to 6
who 29
is very good 3
is a great 7
is a bar 3
is a bit 8
is a good 3
is a nice 3
is the place to 3
is the best 4
is not a 4
is one of 3
...
```