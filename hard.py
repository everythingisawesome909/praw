import praw, re, webbrowser
from datetime import datetime

W  = '\033[0m'  # white
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan

startTime = datetime.now()

user_agent = ("Sifter")

r = praw.Reddit(user_agent = user_agent)

multi_reddits = r.get_subreddit('space+spacex+askreddit+news+todayilearned+worldnews+explainlikeimfive+iama+history+conspiracy+askhistorians+dataisbeautiful+futurology+askreddit+funny+pics+videos+gifs+politics+askpolitics+the_donald+adviceanimals+gaming+wtf+soccer+music+aww+movies+television+books+askscience+science+squaredcircle+showerthoughts+mildlyinteresting+internetisbeautiful+jokes+tifu+fitness+mma+me_irl+technology+politicaldiscussion+tumblrinaction+wow+woahdude+twoxchromosomes+nottheonion+android+legaladvice+lifeprotips+sports+cringe+facepalm+whatcouldgowrong+oddlysatisfying+getmotivated+oldschoolcool+football+personalfinance+whatcouldgowrong+4chan+interestingasfuck+bestof+instant_regret+youdontsurf')

for submission in multi_reddits.get_hot(limit = 250): 
    if re.search("money monsters", submission.title, re.IGNORECASE):
        webbrowser.open(submission.permalink)

print ''+G+''
print datetime.now() - startTime
print ''+W+''
