import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
import random

images = [
    "images/stoic_one.jpeg",
    "images/stoic_two.jpeg",
    "images/stoic_three.jpeg",
    "images/stoic_four.jpeg",
    "images/stoic_five.jpeg",
    "images/stoic_six.jpeg",
]

stoic_quotes = [
    "The obstacle is the way.",
    "You have power over your mind—not outside events. Realize this, and you will find strength.",
    "It is not death that a man should fear, but he should fear never beginning to live.",
    "We suffer more often in imagination than in reality.",
    "The best revenge is not to be like your enemy.",
    "He who fears death will never do anything worth of a man who is alive.",
    "If it is not right, do not do it; if it is not true, do not say it.",
    "Difficulties strengthen the mind, as labor does the body.",
    "The happiness of your life depends upon the quality of your thoughts.",
    "Waste no more time arguing what a good man should be. Be one.",
    "How long are you going to wait before you demand the best for yourself?",
    "You could leave life right now. Let that determine what you do and say and think.",
    "First say to yourself what you would be; and then do what you have to do.",
    "The more we value things outside our control, the less control we have.",
    "Man conquers the world by conquering himself.",
    "Don’t explain your philosophy. Embody it.",
    "To be calm is the highest achievement of the self.",
    "No man is free who is not master of himself.",
    "It’s not what happens to you, but how you react to it that matters.",
    "Self-control is strength. Right thought is mastery. Calmness is power.",
    "The greater the difficulty, the more glory in surmounting it.",
    "Fate leads the willing, and drags along the reluctant.",
    "Luck is what happens when preparation meets opportunity.",
    "To bear trials with a calm mind robs misfortune of its strength and burden.",
    "Wealth consists not in having great possessions, but in having few wants.",
    "Do not act as if you were going to live ten thousand years. Death hangs over you. While you live, while it is in your power, be good.",
    "The soul becomes dyed with the color of its thoughts.",
    "The best way to avenge yourself is to not be like that.",
    "External things are not the problem. It's your assessment of them. Which you can erase right now.",
    "The key is to keep company only with people who uplift you, whose presence calls forth your best.",
    "Receive without pride, let go without attachment.",
    "He who lives in harmony with himself lives in harmony with the universe.",
    "If you want to improve, be content to be thought foolish and stupid.",
    "No great thing is created suddenly.",
    "What we do now echoes in eternity.",
    "Only the educated are free.",
    "Nothing, to my way of thinking, is a better proof of a well-ordered mind than a man’s ability to stop just where he is and pass some time in his own company.",
    "To be stoic is not to be emotionless, but to remain unaffected by your emotions.",
    "Choose not to be harmed, and you won’t feel harmed. Don’t feel harmed, and you haven’t been.",
    "He who is brave is free.",
    "It is not the man who has too little, but the man who craves more, that is poor.",
    "Begin at once to live, and count each separate day as a separate life.",
    "A gem cannot be polished without friction, nor a man perfected without trials.",
    "Stop whatever you’re doing for a moment and ask yourself: Am I afraid of death because I won’t be able to do this anymore?",
    "He who has a why to live can bear almost any how.",
    "Look well into yourself; there is a source of strength which will always spring up if you will always look.",
    "Never let the future disturb you. You will meet it, if you have to, with the same weapons of reason which today arm you against the present.",
    "You always own the option of having no opinion.",
    "If it can be endured, then endure it. Stop complaining.",
    "To live is to endure and be strong.",
    "No man was ever wise by chance.",
    "Life is very short and anxious for those who forget the past, neglect the present, and fear the future.",
    "The robbed that smiles steals something from the thief.",
    "How ridiculous and how strange to be surprised at anything which happens in life.",
    "People are not disturbed by things, but by the views they take of them.",
    "The universe is change; our life is what our thoughts make it.",
    "While we wait for life, life passes.",
    "Cling tooth and nail to the following rule: not to give in to adversity, not to trust prosperity, and always take full note of fortune’s habit of behaving just as she pleases.",
    "A man’s worth is no greater than his ambitions.",
    "We must indulge the mind and from time to time allow it the leisure which is its food and strength.",
    "Freedom is the only worthy goal in life. It is won by disregarding things that lie beyond our control.",
    "The art of living is more like wrestling than dancing.",
    "When you arise in the morning, think of what a privilege it is to be alive, to think, to enjoy, to love.",
    "Wherever there is a human being, there is an opportunity for kindness.",
    "Let us prepare our minds as if we'd come to the very end of life. Let us postpone nothing. Let us balance life’s books each day.",
    "No one can escape pain, fear, and suffering. Yet we all strive for happiness. Only those who understand the nature of life find it.",
    "If a man knows not which port he sails, no wind is favorable.",
    "Remember, it is not enough to be hit or insulted to be harmed. You must believe that you are being harmed.",
    "If you are pained by any external thing, it is not this thing that disturbs you, but your own judgment about it. And it is in your power to wipe out this judgment now.",
    "To love only what happens, what was destined. No greater harmony.",
    "Look not round at the depraved morals of others, but run straight along the line without deviating from it.",
    "Time is like a river made up of the events which happen, and a violent stream; for as soon as a thing has been seen, it is carried away, and another comes in its place, and this will be carried away too.",
    "Today I escaped anxiety. Or no, I discarded it, because it was within me, in my own perceptions — not outside.",
    "Be tolerant with others and strict with yourself.",
    "You become what you give your attention to.",
    "What is to give light must endure burning.",
    "To understand the true quality of people, you must look into their minds, and examine their pursuits and aversions.",
    "True happiness is to enjoy the present, without anxious dependence upon the future.",
    "Whatever happens, it happens for good, and it is in your best interest to embrace it.",
    "The impediment to action advances action. What stands in the way becomes the way.",
    "Be content with what you have; rejoice in the way things are. When you realize there is nothing lacking, the whole world belongs to you.",
    "Don’t seek for everything to happen as you wish it would, but rather wish that everything happens as it actually will—then your life will flow well.",
    "Every new beginning comes from some other beginning’s end.",
    "What we fear doing most is usually what we most need to do.",
    "Nothing endures but change.",
    "Silence is a lesson learned through life’s many sufferings.",
    "He who has learned how to die has unlearned how to be a slave.",
    "Do what you can, with what you have, where you are.",
    "To live a good life: We have the potential for it. If we learn to be indifferent to what makes no difference.",
    "The whole future lies in uncertainty: live immediately.",
    "Whatever can happen at any time can happen today.",
    "No man is crushed by misfortune unless he has first been deceived by prosperity."
]

load_dotenv()

token = getenv("DISCORD_TOKEN")

# Setting up intents for your bot to send messages
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('dkhl dekchi li khass :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("rak m3adek ta9lwa :angry:")

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.send("ha9 mcha")
    await member.ban(reason = reason)

#The below code unbans player.
@bot.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')


@bot.command(aliases=["av"])
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    embed = discord.Embed(
        title=f"{member.name}'s Avatar",
        color=discord.Color.green()
    )
    embed.set_image(url=member.avatar.url)
    await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
            
    if message.content.startswith("$quote"):
        random_quote_number = random.randint(0, len(stoic_quotes) - 1)
        random_image_number = random.randint(0, len(images) - 1)
        selected_quote = stoic_quotes[random_quote_number]
        image_path = images[random_image_number]

        embed = discord.Embed(
            title="Stoic Quote",
            description=selected_quote,
            color=discord.Color.green()
        )

        # Send the message with the quote and attach the image
        with open(image_path, 'rb') as image_file:
            file = discord.File(image_file, filename=image_path.split("/")[-1])
            embed.set_image(url=f"attachment://{file.filename}")
            await message.channel.send(embed=embed, file=file)

    # Process commands if there are any
    await bot.process_commands(message)

bot.run(token)