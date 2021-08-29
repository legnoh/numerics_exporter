import json
import modules.numerics.numerics as nj

card = nj.NumericsIo()

with open('origin/moneyforward.json', mode='rt', encoding='utf-8') as file:
  mf_data = json.load(file)


# 01. 当月収支をでかく表示

monthly_balance = mf_data['当月収支']['当月収支']

## 10万以上なら緑、残金5万以下ならオレンジ、負債になっていたら赤
if monthly_balance >= 100000:
  color = "green"
elif 50000 <= monthly_balance:
  color = "orange"
elif monthly_balance < 0:
  color = "red"
else:
  color = None

monthly_balance_result = card.get_number("当月収支(¥)", monthly_balance, color)
with open('public/money_monthly_balance.json', 'w', encoding='utf-8') as stream:
    json.dump(monthly_balance_result, stream)


# 02. 現在の資産バランスシートを奨学金・年金を抜いて計算

## 資産から年金額を除外
portfolio = mf_data['資産']['資産総額'] - mf_data['資産']['内訳']['年金']['合計']

## 負債から奨学金を除外
liability = mf_data['負債']['負債総額']
for debt in mf_data['負債']['内訳']:
  if debt['種類'] == '奨学金':
    liability -= debt['残高']

total_balance = portfolio - liability

## 0円以下の場合は赤、50万円以上の場合はオレンジ、120万円以上の場合は緑
if total_balance < 0:
  color = "red"
elif total_balance <= 500000:
  color = "orange"
elif total_balance >= 1200000:
  color = "green"
else:
  color = None

total_balance_result = card.get_number("バランスシート", total_balance, color)

with open('public/money_reality_balance.json', 'w', encoding='utf-8') as stream:
    json.dump(total_balance_result, stream)


# 03. SBIネット銀行の残高

sbi_account = next(
  item for item in mf_data['資産']['内訳']['預金・現金・暗号資産']['口座情報'] if item["種類・名称"] == "代表口座 - 普通"
)

sbi_balance_result = card.get_number("SBI銀行残高", sbi_account['残高'])

with open('public/money_sbi_balance.json', 'w', encoding='utf-8') as stream:
    json.dump(sbi_balance_result , stream)
