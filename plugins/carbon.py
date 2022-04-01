Bot.command('carbon', async ctx => { 
ctx.reply("*Welcome!*\n_You can use me to Carbon for your texts And Codes!\nJust what to do? Send me a text, I'll convert it to Carbon Image then!_",{parse_mode: "MARKDOWN"});
  ctx.question('carbon')
  })
// This Module Created By https://telegram.me/rex_botz
Bot.on('answer', 'carbon', async ctx => {
var msg = ""+encodeURI(ctx.message.text+"")
var url = 'https://carbonnowsh.herokuapp.com/?code='+msg+'&backgroundColor=black'
// you can easily modifly color by changing color=black to another like Color=red
ctx.reply("`💠 Generating Carbon Please Wait.....`",{parse_mode: "MARKDOWN"});
 ctx.api.sendPhoto(ctx.from.id, url, {
    caption: "💠Succefully Generated Carbon Image"
  })

});
