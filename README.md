# Attendance Tracker

## Description
A simple attendance tracking system developed with Python and Tkinter. It records employee attendance time by card number and displays corresponding employee ID and name.

## Features
- Real-time display of current time.
- Users record attendance by entering card numbers.
- Reads card number to employee ID and name mapping from `card_to_employee.txt`.

## How to Use
1. Clone the repository: `git clone [repository URL]`
2. Run `records.py`.
3. Ensure `card_to_employee.txt` is in the same directory and correctly formatted.

## Dependencies
- Python 3
- Tkinter library

# Attendance Tracker Update 2023-12-18

- Implemented the feature to record the first and last card swipes as start and end of the workday.
- Added functionality to automatically export daily attendance records to an Excel file at a specified time (e.g., end of the workday), named with the date.
- Enhanced flexibility for easy adaptation to different site names.
- Fixed minor errors and optimized code structure.

# 勤怠トラッカー

## 説明
PythonとTkinterで開発されたシンプルな勤怠追跡システムです。カード番号で従業員の出勤時間を記録し、対応する従業員IDと名前を表示します。

## 特徴
- 現在時刻のリアルタイム表示。
- ユーザーはカード番号を入力して出勤を記録します。
- `card_to_employee.txt`からカード番号と従業員ID、名前のマッピングを読み取ります。

## 使い方
1. リポジトリをクローン：`git clone [リポジトリURL]`
2. `records.py`を実行します。
3. `card_to_employee.txt`が同じディレクトリにあり、正しくフォーマットされていることを確認します。

## 依存関係
- Python 3
- Tkinterライブラリ

# 勤怠トラッカーの更新 2023-12-18

- 初回と最終のカードスワイプを勤務開始と終了として記録する機能を実装しました。
- 指定時間（例：業務終了時）にその日の勤怠記録をExcelファイルに自動的にエクスポートする機能を追加しました。ファイル名は日付で命名されます。
- 異なるサイト名に簡単に対応できる柔軟性を向上しました。
- 細かなエラーを修正し、コード構造を最適化しました。

# 出勤追蹤系統

## 描述
這是一個使用Python和Tkinter開發的簡易出勤追蹤系統。它能夠通過卡號記錄員工的出勤時間，並顯示對應的工號和姓名。

## 功能
- 實時顯示當前時間。
- 使用者透過輸入卡號記錄出勤。
- 從 `card_to_employee.txt` 檔案讀取卡號至工號和姓名的對應資訊。

## 使用方法
1. 克隆倉庫：`git clone [倉庫URL]`
2. 執行 `records.py`。
3. 確保 `card_to_employee.txt` 檔案位於同一目錄下，且格式正確。

## 依賴項
- Python 3
- Tkinter庫

# 出勤追蹤系統更新 2023-12-18

- 實現了將每日第一次和最後一次刷卡記錄為工作日開始和結束的功能。
- 增加了在指定時間（例如工廠下班時間）自動將當日出勤記錄匯出為Excel檔案的功能，檔案以日期命名。
- 增強了便於適應不同站點名稱的靈活性。
- 修正了小錯誤並優化了代碼結構。
