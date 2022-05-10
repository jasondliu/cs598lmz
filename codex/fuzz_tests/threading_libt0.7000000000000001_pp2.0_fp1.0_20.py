import threading
threading.Thread(target=scraper.main).start()

@bot.command(pass_context=True)
async def new_member(ctx, member : discord.Member = None):
    if member is None:
        await bot.say('Invalid user.')
        return
    if not member.server_permissions.manage_roles:
        await bot.say('User does not have the Manage Roles permission.')
        return
    role = discord.utils.get(ctx.message.server.roles, name='New Member')
    await bot.add_roles(member, role)
    await bot.say(member.mention + ' has been given the New Member role.')

@bot.command(pass_context=True)
async def clear_roles(ctx, member : discord.Member = None):
    if member is None:
        await bot.say('Invalid user.')
        return
    if not member.server_permissions.manage_roles:
        await bot.say('User does not have the Manage Roles permission.')
        return
