import pytesseract
from PIL import ImageGrab
import pyautogui
import sys
import time

# Tesseractのパスを設定
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def click_color_button(target_text):
    # スクリーンショットを取得
    print(f"{target_text}ボタンを探しています...")
    screenshot = ImageGrab.grab()
    
    # OCR処理を実行
    ocr_result = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)
    
    # OCR結果から指定された色のテキストを検索
    found_index = None
    
    for i, text in enumerate(ocr_result['text']):
        if text.strip():
            if text.lower() == target_text.lower():
                found_index = i
                break
    
    if found_index is None:
        print(f'"{target_text}"が画面上で見つかりませんでした。')
        return False
    
    # クリック座標を計算
    click_x = ocr_result['left'][found_index] + ocr_result['width'][found_index] // 2
    click_y = ocr_result['top'][found_index] + ocr_result['height'][found_index] // 2
    
    print(f'"{target_text}" が見つかりました。クリックを実行します...')
    print(f"クリック座標: x={click_x}, y={click_y}")
    
    # クリックを実行
    pyautogui.click(click_x, click_y)
    print(f'"{target_text}" をクリックしました。')
    return True

def main():
    # 色の順序を定義
    colors = ["red", "green", "blue"]
    
    try:
        for color in colors:
            # 指定された色のボタンをクリック
            if not click_color_button(color):
                print(f"{color}ボタンのクリックに失敗しました。")
                sys.exit(1)
            
            # 5秒待機
            print(f"5秒待機します...")
            time.sleep(5)
            
        print("すべての色のボタンのクリックが完了しました。")
        
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()