#!/bin/bash

# 搜尋 images 資料夾中的所有 .jpeg 檔案，並將它們重新命名為 .jpg
find images -type f -name "*.jpeg" | while read file; do
    # 取得檔案的目錄和基本名稱
    dir=$(dirname "$file")
    base=$(basename "$file" .jpeg)
    
    # 重新命名檔案
    mv "$file" "$dir/$base.jpg"
    
    # 顯示處理的檔案
    echo "已重新命名: $file -> $dir/$base.jpg"
done

echo "所有 .jpeg 檔案已重新命名為 .jpg"