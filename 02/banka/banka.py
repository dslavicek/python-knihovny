# Nasimulujte bankovní systém
#
# V adresáři jsou soubory pojmenované číslem účtu obsahující zůstatek účtu
# Implementujte skript banka.py, který bude ovládán parametry:
#
# Částka se bude čerpat z účtu 111 pomocí --from 111
# Částka se bude připisovat na účet 222 pomocí --to 222
# Převod částky 1000 se určí parametrem --amount 1000
#
# Snažte se řešit různé chyby:
# * účet neexistuje
# * zůstatek by šel do záporu
#
# Příklad použití:
#
#   python banka.py --from 111 --to 222 --amount 1000
#
# V praxi se píší skripty, kde nezáleží na pořadí pojmenovaných parametrů, tj.
# ideální je, když funguje libovolné pořadí parametrů při spuštění:
#
#   python banka.py --from 111 --amount 1000 --to 222
#   python banka.py --amount 1000 --from 111 --to 222
#
# Pro tento pokročilý způsob je však třeba použít pokročilou knihovnu pro práci
# s parametry příkazové řádky, jako např. argparse nebo click.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--from",
    type=str,
    help="senders_account",
    required=True,
    dest="from_account")

parser.add_argument(
    "--to",
    type=str,
    help="senders_account",
    required=True)

parser.add_argument(
    "--amount",
    type=int,
    help="senders_account",
    required=True)

args = parser.parse_args()

try:
    with open(args.from_account)as f:
        senders_balance = int(f.read())
except:
    print("sender's account does not exist or is broken")
    exit()

try:
    with open(args.to)as f:
        receivers_balance = int(f.read())
except:
    print("sender's account does not exist or is broken")
    exit()

if senders_balance < args.amount:
    print("Not enough money!")
    exit()

receivers_balance += args.amount
senders_balance -= args.amount

with open(args.from_account, "w")as f:
    f.write(str(senders_balance))

with open(args.to, "w")as f:
    f.write(str(receivers_balance))
