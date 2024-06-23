import os
import re

release_path_map = {
    'all': {
        'title': '仑质 的 命运2 DIM愿望单',
        'description': '仑质制作的DIM愿望单，自用，包含大量个人向内容，不保证质量，不保证更新，不保证完整，不保证可用，不保证可玩，不保证可读',
        'path': 'sublist'
    }
}

release_map = {}

if __name__ == '__main__':
    print('Release all start')
    for map_key, map_value in release_path_map.items():
        tmp_path_list = [
            os.path.join(map_value['path'], file_this)
            for file_this in os.listdir(map_value['path'])
        ]
        tmp_path_list.sort()
        release_map[map_key] = tmp_path_list
    print(release_map)
    for release_key, release_value in release_map.items():
        release_file_str_list = [(
            f"title:{release_path_map[release_key]['title']}\n"
            f"description:{release_path_map[release_key]['description']}\n"
        )]
        for release_file_src in release_value:
            print(f'loading {release_file_src} ...')
            with open(release_file_src, 'r', encoding='utf-8') as f:
                release_file_str_this = f.read()
                release_file_str_this = re.sub(r'^title:',       '@title:',       release_file_str_this)
                release_file_str_this = re.sub(r'\ndescription:', '\n@description:', release_file_str_this)
                release_file_str_list.append(release_file_str_this)
        with open(f'{release_key}.txt', 'w', encoding='utf-8') as f:
            f.write(('\n' * 6).join(release_file_str_list))
    print('Release all done')
