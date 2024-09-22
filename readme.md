#模糊系統範例 - 根據身高和體重評估體型

本項目使用 Python 和 scikit-fuzzy 庫建立了一個簡單的模糊系統，根據輸入的身高和體重評估一個人的體型。透過模糊邏輯和隸屬度函數，該系統能夠處理不確定性，並給出合理的體型評估結果。

模糊系統是一種基於模糊邏輯的計算模型，能夠處理模糊和不精確的資訊。本項目透過建立模糊集合、定義模糊規則，以及執行模糊推理，實現了對體型的評估。該系統適用於教育目的，展示了模糊系統的基本原理和實現方法。

## 先決條件
在開始之前，請確保您已經安裝了以下軟體：

Python 3.x
scikit-fuzzy 庫
matplotlib 庫

## 安裝

請按照以下步驟安裝必要的庫：
```
pip install scikit-fuzzy matplotlib
```


範例說明
以下是主要的程式碼片段和說明：

1. 導入庫
```
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt
```

2. 定義輸入和輸出變數
```
# 輸入變數
height = ctrl.Antecedent(np.arange(140, 201, 1), 'height')
weight = ctrl.Antecedent(np.arange(40, 121, 1), 'weight')
```

# 輸出變數
body_type = ctrl.Consequent(np.arange(0, 11, 1), 'body_type')
3. 定義模糊集合並繪製隸屬度函數
```
# 身高的模糊集合
height['short'] = fuzz.trimf(height.universe, [140, 140, 160])
height['average'] = fuzz.trimf(height.universe, [150, 170, 190])
height['tall'] = fuzz.trimf(height.universe, [170, 200, 200])
```

# 繪製身高的隸屬度函數
height.view()
4. 定義模糊規則
```
rule1 = ctrl.Rule(height['short'] & weight['light'], body_type['average'])
rule2 = ctrl.Rule(height['short'] & weight['medium'], body_type['fat'])
```

# 其他規則省略
5. 建立控制系統並進行模擬
```
body_type_ctrl = ctrl.ControlSystem([rule1, rule2, ...])
body_type_simulation = ctrl.ControlSystemSimulation(body_type_ctrl)
```

6. 輸入數值並計算結果
```
body_type_simulation.input['height'] = 175
body_type_simulation.input['weight'] = 65
body_type_simulation.compute()
print("體型評估結果：", body_type_simulation.output['body_type'])
```

7. 視覺化輸入和輸出
```
height.view(sim=body_type_simulation)
weight.view(sim=body_type_simulation)
body_type.view(sim=body_type_simulation)
plt.show()
```

## 視覺化結果
執行程式後，您將看到以下結果：

隸屬度函數圖形：展示了輸入和輸出變數的模糊集合。
輸入值位置：在隸屬度函數圖上顯示了當前輸入值的位置。
輸出結果圖：展示了體型評估的模糊輸出和解模糊化結果。
## 自訂調整
您可以通過以下方式自訂該模糊系統：

修改輸入值：更改 body_type_simulation.input['height'] 和 body_type_simulation.input['weight'] 的值，觀察結果如何變化。
調整模糊集合：修改隸屬度函數的形狀和範圍，例如使用 gaussmf、gbellmf 等函數。
添加或修改規則：根據實際需求，添加新的模糊規則或調整現有規則。
## 參考資源
scikit-fuzzy 官方文檔：https://scikit-fuzzy.github.io/scikit-fuzzy/
Matplotlib 官方文檔：https://matplotlib.org/