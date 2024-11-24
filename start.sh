if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://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@github.com/AreBhaai/Mrbean.git /Elsa
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Elsa
fi
cd /Elsa
pip3 install -U -r requirements.txt
echo "STARING...."
python3 bot.py
