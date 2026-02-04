# upyoung_Automation_Test_Enginee_HW

本專案包含兩個作業：
- **HW1_Playwright Automation Test Challenge**：使用 Python + Poetry + Playwright（Chromium）（含 Page Object Pattern）。(花費：50 分鐘)
- **HW2_API Testing Challenge**：使用 Postman Echo Collection 完成 API 正向/負向測試（可用 Postman GUI）。(花費：20 分鐘)

---

## Prerequisites（前置需求）

### HW1（Playwright / Python）
- Python **3.13+**（建議使用 pyenv 或 Homebrew 安裝）
- Poetry（2.x）
- macOS / Linux / Windows 皆可（本專案以 macOS 測試）

## 執行步驟

1. 進入 HW1 專案目錄  
2. 安裝相依套件  
   ```bash
   poetry install --no-root
   ```
3.	安裝 Playwright Chromium 瀏覽器
     ```bash
    poetry run playwright install chromium
    ```   
4. 執行自動化測試
    ```bash
    poetry run pytest
    ```

## 備註: 目前跑完測試會出現錯誤：
   ```bash
    AssertionError: assert 'Thank you for your order!' == 'THANK YOU FOR YOUR ORDER'
```

是因為照著作業指示的字串來驗證 "THANK YOU FOR YOUR ORDER"，與實際有差異，因此這個測試項目固定會 Fail。
    

### HW2（Postman / API）
- Postman Desktop App（建議最新版）
## 執行步驟（Postman GUI）
	1.	開啟 Postman
	2.	Import 專案 HW2 資料夾內提供的 Postman Collectio（.json）
    
	3.	執行測試：
	•	單一 Request：點擊 Send
	•	整包測試：使用 Collection Runner
