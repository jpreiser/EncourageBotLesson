# Discord Bot Project
[https://www.youtube.com/watch?v=SPTfmiYiuok&list=WL&index=73]
### 6/9/23
### Takeaways
- discordpy library for using clients, events, and async in order to communicate. 
- Discord developer tool for generating disord bot

#### First Issue
>First deviation from tutorial based on out-dated information involved using a different api source, the process of retrieving via api call and parsing received information to be returned to the user. 

#### Second Issue
>Bot was responding to PMs but not in general channels, realized discord.Client(intentions) needed to be changed to all() from default() and specific permissions granted to the bot from the developer portal. 
- Create list for bot to listen for to reply automatically 
	+ functionality of continual listening and scanning of messages for keywords
- Update bot from discord with input from users