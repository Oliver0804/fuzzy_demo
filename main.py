import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

# 定義輸入和輸出變數
height = ctrl.Antecedent(np.arange(140, 201, 1), 'height')
weight = ctrl.Antecedent(np.arange(40, 121, 1), 'weight')
body_type = ctrl.Consequent(np.arange(0, 11, 1), 'body_type')

# 定義模糊集合並繪製隸屬度函數
height['short'] = fuzz.trimf(height.universe, [140, 140, 160])
height['average'] = fuzz.trimf(height.universe, [150, 170, 190])
height['tall'] = fuzz.trimf(height.universe, [170, 200, 200])

# 繪製身高的隸屬度函數
height.view()

weight['light'] = fuzz.trimf(weight.universe, [40, 40, 60])
weight['medium'] = fuzz.trimf(weight.universe, [50, 70, 90])
weight['heavy'] = fuzz.trimf(weight.universe, [80, 120, 120])

# 繪製體重的隸屬度函數
weight.view()

body_type['thin'] = fuzz.trimf(body_type.universe, [0, 0, 5])
body_type['average'] = fuzz.trimf(body_type.universe, [3, 5, 7])
body_type['fat'] = fuzz.trimf(body_type.universe, [5, 10, 10])

# 繪製體型的隸屬度函數
body_type.view()

# 定義規則
rule1 = ctrl.Rule(height['short'] & weight['light'], body_type['average'])
rule2 = ctrl.Rule(height['short'] & weight['medium'], body_type['fat'])
rule3 = ctrl.Rule(height['short'] & weight['heavy'], body_type['fat'])

rule4 = ctrl.Rule(height['average'] & weight['light'], body_type['thin'])
rule5 = ctrl.Rule(height['average'] & weight['medium'], body_type['average'])
rule6 = ctrl.Rule(height['average'] & weight['heavy'], body_type['fat'])

rule7 = ctrl.Rule(height['tall'] & weight['light'], body_type['thin'])
rule8 = ctrl.Rule(height['tall'] & weight['medium'], body_type['thin'])
rule9 = ctrl.Rule(height['tall'] & weight['heavy'], body_type['average'])

# 建立控制系統
body_type_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

# 如果想要視覺化規則，可以視覺化單個規則
# rule1.view()
# rule2.view()
# rule3.view()
# 依此類推

# 建立模糊控制系統模擬
body_type_simulation = ctrl.ControlSystemSimulation(body_type_ctrl)

# 輸入數值
body_type_simulation.input['height'] = 175
body_type_simulation.input['weight'] = 65

# 執行模糊推理
body_type_simulation.compute()

# 輸出結果
print("體型評估結果：", body_type_simulation.output['body_type'])

# 繪製輸入變數的隸屬度函數並顯示輸入值
height.view(sim=body_type_simulation)
weight.view(sim=body_type_simulation)

# 繪製輸出變數的隸屬度函數並顯示輸出值
body_type.view(sim=body_type_simulation)

# 如果需要繪製控制面，可以使用以下程式碼
# 生成輸入變數的網格
height_range = np.arange(140, 201, 5)
weight_range = np.arange(40, 121, 5)
height_grid, weight_grid = np.meshgrid(height_range, weight_range)

# 初始化輸出網格
body_type_output = np.zeros_like(height_grid)

# 計算輸出值
for i in range(height_grid.shape[0]):
    for j in range(height_grid.shape[1]):
        body_type_simulation.input['height'] = height_grid[i, j]
        body_type_simulation.input['weight'] = weight_grid[i, j]
        body_type_simulation.compute()
        body_type_output[i, j] = body_type_simulation.output['body_type']

# 繪製控制面
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(height_grid, weight_grid, body_type_output, cmap='viridis')
ax.set_xlabel('Height')
ax.set_ylabel('Weight')
ax.set_zlabel('Body Type')
plt.show()

