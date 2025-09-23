#!/bin/bash

# 讓使用者輸入搜尋路徑，預設為 images
read -p "請輸入搜尋路徑 (預設為 images): " search_path
search_path=${search_path:-images}

# 檢查路徑是否存在
if [ ! -d "$search_path" ]; then
    echo "錯誤: 路徑 '$search_path' 不存在或不是目錄"
    exit 1
fi

# 搜尋指定資料夾中的所有 .jpeg 檔案，並將它們重新命名為 .jpg
find "$search_path" -type f -name "*.jpeg" | while read file; do
    # 取得檔案的目錄和基本名稱
    dir=$(dirname "$file")
    base=$(basename "$file" .jpeg)
    
    # 重新命名檔案
    mv "$file" "$dir/$base.jpg"
    
    # 顯示處理的檔案
    echo "已重新命名: $file -> $dir/$base.jpg"
done

echo "所有 .jpeg 檔案已重新命名為 .jpg"