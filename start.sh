if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Tanujairam123/Rex-filter-bot.git /Rex-filter-bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Rex-filter-bot
fi
cd /Rex-filter-bot
pip3 install -U -r requirements.txt
echo "Starting rex bot 🔥🔥🔥.........."
python3 bot.py
