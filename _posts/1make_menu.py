import os

def generate_md_index(root_dir, output_file):
    def walk_dir(dir_path, level=0):
        lines = []
        entries = sorted(os.listdir(dir_path))
        for entry in entries:
            full_path = os.path.join(dir_path, entry)
            rel_path = os.path.relpath(full_path, root_dir).replace("\\", "/")
            if os.path.isdir(full_path):
                lines.append("  " * level + f"- **{entry}**")
                lines.extend(walk_dir(full_path, level + 1))
            elif entry.lower().endswith(".md"):
                name = os.path.splitext(entry)[0]
                lines.append("  " * level + f"- [{name}]({rel_path})")
        return lines

    lines = ["# Markdown 文件目录", ""]
    lines.extend(walk_dir(root_dir))

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))

    print(f"生成完成，目录保存在 {output_file}")

if __name__ == "__main__":
    root_dir = r"E:\github\resume\_posts"
    output_file = r"E:\github\resume\_posts\0目录.md"
    generate_md_index(root_dir, output_file)
