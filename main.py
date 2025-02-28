from fastapi import FastAPI
import random
import uvicorn
from fastapi.responses import RedirectResponse
import urllib.parse

app = FastAPI()

tweets = [
    "Just joined the #MoveWithAI buildathon! Excited to be part of this innovative event with @Aptos, @JouleFinance, and @metamove_. Can't wait to see what we create! #Buildathon #DeveloperLife 🚀",
    "The #MoveWithAI buildathon is on! Working alongside amazing minds and supported by @Aptos, @JouleFinance, and @metamove_. Ready to build something great! #TechEvent #Innovation 💡",
    "Nothing excites a developer more than a buildathon! #MoveWithAI is off to an incredible start with @Aptos, @JouleFinance, and @metamove_ leading the way. Let's go! #Coding #Community 👨‍💻",
    "The energy at the #MoveWithAI buildathon is unreal! Grateful to @Aptos, @JouleFinance, and @metamove_ for fostering such an innovative space. Let’s build the future! #TechEvent 🔥",
    "Midway through the #MoveWithAI buildathon and ideas are flowing! Thanks to @Aptos, @JouleFinance, and @metamove_ for the support. Excited to see the final projects! #Development #Innovation 🎯",
    "Brainstorming at the #MoveWithAI buildathon! The creativity is next level. Shoutout to @Aptos, @JouleFinance, and @metamove_ for bringing builders together! #TechCommunity 🚀",
    "The #MoveWithAI buildathon is in full swing! Developing alongside top minds with @Aptos, @JouleFinance, and @metamove_. Let's shape the future! #TechEvent 💻",
    "Just hit a milestone at the #MoveWithAI buildathon! Thanks @Aptos, @JouleFinance, and @metamove_ for making this possible. Excited for what’s next! #Development #Tech 🎯",
    "The #MoveWithAI buildathon is nearing the finish line! What an experience, thanks to @Aptos, @JouleFinance, and @metamove_. Unforgettable journey! #TechChallenge #DeveloperLife 🎉",
    "Wrapping up the #MoveWithAI buildathon with a sense of achievement. Thanks to @Aptos, @JouleFinance, and @metamove_ for making it all possible! #TechCommunity #Innovation 🚀",
    "The #MoveWithAI buildathon has been a blast! Final projects coming together, all thanks to @Aptos, @JouleFinance, and @metamove_. Let’s innovate! #TechEvent 💡",
    "That’s a wrap! The #MoveWithAI buildathon has been an incredible ride with @Aptos, @JouleFinance, and @metamove_. Can't wait to see what we create next! #DeveloperLife #Tech 🎯",
    "The #MoveWithAI buildathon has been an unforgettable experience. Huge thanks to @Aptos, @JouleFinance, and @metamove_ for bringing builders together. #TechChallenge #Innovation 🔥",
    "The creativity at the #MoveWithAI buildathon was unmatched! Thanks @Aptos, @JouleFinance, and @metamove_ for fueling innovation. Let’s keep building! #TechCommunity 🚀",
    "Final moments of the #MoveWithAI buildathon! Reflecting on an amazing journey with @Aptos, @JouleFinance, and @metamove_. The future looks bright! #TechEvent 💡",
    "Just presented our project at the #MoveWithAI buildathon! Huge shoutout to @Aptos, @JouleFinance, and @metamove_ for this opportunity. #Innovation #Development 🎉",
    "The #MoveWithAI buildathon has been inspiring. The support from @Aptos, @JouleFinance, and @metamove_ has been invaluable. Let’s keep innovating! #TechCommunity #DeveloperLife 🚀",
    "What a journey! The #MoveWithAI buildathon has pushed us to innovate and grow. Grateful to @Aptos, @JouleFinance, and @metamove_ for making it possible. #TechChallenge 💡",
    "The #MoveWithAI buildathon has been a wild ride of creativity and problem-solving! Thanks to @Aptos, @JouleFinance, and @metamove_ for an amazing experience! #TechEvent 🎯",
    "We built, we innovated, we delivered! Huge thanks to @Aptos, @JouleFinance, and @metamove_ for powering the #MoveWithAI buildathon. Until next time! #DeveloperLife 🚀",
    "Just had an amazing time at the #MoveWithAI buildathon! The energy, the ideas, the community—everything was top-notch. Thanks @Aptos, @JouleFinance, and @metamove_! #TechChallenge 🔥",
    "The #MoveWithAI buildathon has been a dream for developers. Grateful to @Aptos, @JouleFinance, and @metamove_ for making it happen. Can’t wait for the next one! #TechEvent 💡",
    "The #MoveWithAI buildathon was an innovation-packed experience! Thanks @Aptos, @JouleFinance, and @metamove_ for pushing us to build the future. #TechCommunity 🚀",
    "Final submission done at the #MoveWithAI buildathon! What an incredible event, thanks to @Aptos, @JouleFinance, and @metamove_ for the opportunity! #DeveloperLife 🎯",
    "The #MoveWithAI buildathon tested our skills, pushed our limits, and connected us with brilliant minds. Thank you @Aptos, @JouleFinance, and @metamove_! #TechEvent 🔥",
    "Innovation, creativity, and collaboration defined the #MoveWithAI buildathon. Thanks @Aptos, @JouleFinance, and @metamove_ for making it possible! #TechChallenge 🚀",
    "Wrapping up the #MoveWithAI buildathon on a high note! Big thanks to @Aptos, @JouleFinance, and @metamove_ for this opportunity. #TechEvent 💡",
    "What a ride! The #MoveWithAI buildathon was everything a developer could ask for. Thanks to @Aptos, @JouleFinance, and @metamove_ for the support! #TechCommunity 🚀",
    "The #MoveWithAI buildathon was a rollercoaster of ideas and execution! Thanks @Aptos, @JouleFinance, and @metamove_ for making it happen. #DeveloperLife 🎯",
    "Looking back at the #MoveWithAI buildathon, I’m proud of what we built! Big thanks to @Aptos, @JouleFinance, and @metamove_ for making it all possible! #TechChallenge 🔥"
]

@app.get("/tweet")
def redirect_to_tweet():
    tweet = random.choice(tweets)
    encoded_tweet = urllib.parse.quote(tweet)  # Properly encode the tweet
    tweet_url = f"https://x.com/intent/tweet?text={encoded_tweet}"
    return RedirectResponse(url=tweet_url)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
