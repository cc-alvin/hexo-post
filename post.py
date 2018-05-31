import time
import os
import config
import pinyin_util

separate = '---\n'
title_pattern = 'title: {} \n'
tags_pattern = 'tags: \n - {}'
categories_pattern = 'categories:  \n - {}'
date_pattern = 'date: {} \n'


def create_file(title, tags, categories, content):
    file_name = 'mds/'+'_'.join(pinyin_util.wordToPinyin(title)) + '.md'
    file_name=''.join(file_name.split())
    with open(file_name, 'w') as f:
        # title
        post_title = title_pattern.format(title)

        # tags
        tags = tags.split(',')
        tags_items = map(addNewLineFlag, tags)
        post_tags = tags_pattern.format(' - '.join(tags_items))

        # categories
        categories = categories.split(',')
        categories_items = map(addNewLineFlag, categories)
        post_categories = categories_pattern.format(' - '.join(categories_items))

        # date
        date = date_pattern.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        post_content = content + '\n'

        f.write(separate)
        f.write(post_title)
        f.write(post_tags)
        f.write(post_categories)
        f.write(date)
        f.write(separate)
        f.write('\n')
        f.write('\n')
        f.write(post_content)
        return os.path.realpath(f.name)


def addNewLineFlag(s):
    return s + '\n'


def publish(title, tags, categories, content):
    path = create_file(title=title, tags=tags, categories=categories, content=content)
    ret = os.popen('sh shell/publish.sh {} {}'.format(config.root_path, path))
    return ret.read()


if __name__ == '__main__':
    title = 'Hello'
    tags = 'java'
    categories = 'Develop'
    content = '# 123456'
    ret = publish(title=title, tags=tags, categories=categories, content=content)
    print(ret)
