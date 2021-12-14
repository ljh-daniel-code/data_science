import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm


plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)

travel = pd.read_csv("data\\traveling.csv")
print(travel)

#남성, 여성들이 충북에서 다른 지역으로 이동하는 정도 순위
condition1 = travel["Start"] == "충청북도"
condition2 = travel["Age"] == 20
condition3 = travel["Gender"] == 1
condition4 = travel["Gender"] == 2

Home1 = travel.loc[condition1 & condition2 & condition3]
Home2 = travel.loc[condition1 & condition2 & condition4]

print(Home1.sort_values(by="People", ascending=False).head(16))
print(Home2.sort_values(by="People", ascending=False).head(16))

#충북에서 울산으로 이동 남녀, 나이별 그래프
condition5 = travel["Start"] == "충청북도"
condition6 = travel["End"] == "울산광역시"
place = travel.loc[condition5 & condition6]
table = pd.pivot_table(data=place, index=["Age"], columns=["Gender"], values=["People"])
table.plot(kind="bar")
print(table)
plt.show()

#충북에서 각지역별로 이동하는 사람들의 수
condition7 = travel["Start"] == "충청북도"
move = travel.loc[condition7]
table = pd.pivot_table(data=travel, index=["Gender"], columns=["End"], values=["People"])
table.plot(kind="bar")
print(table)
plt.show()