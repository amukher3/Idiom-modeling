### Idiom-modeling 

This is an effort to model english language idiom using Topic modeling. The topic modeling approach used here is the Latent
Dirchelet's allocation(LDA). One of the potential applications of this effort is to get the appropriate idiom from its corresponding meaning or even from the "bits and pieces" of its english language meaning. 

I used whatever data that I could gather from various web pages. This task required some data-cleaning. 
With the current database, its usage is pretty limited but with a increase in the size of the database(i.e adding more idioms) and with a better `similarity metric` this method of getting the idiom from its english language meaning or even from the parts of its meaning might turn out to be more than handy. 

Other methods of modeling the topic such as `matrix factorization` can also be used to check its effectiveness in comparison to `LDA`. 

This is still work in progress. I intend to add some vizualisations to show the clusters of the topics also may be try out with other topic models and make it more dependent on topic modeling approach. 

I also intend to improve the user interface and deploy it using Flask or maybe a docker container. 

Future approach --- use word embedding based similarity metric i.e a `similarity measure which takes the feature of the word into account` while calculating similarity. Recommended package will be from Gensim. 
