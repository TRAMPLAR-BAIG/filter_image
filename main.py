from ImageHash import ImageHashHandler


def main():
    handler = ImageHashHandler('/path/to/pictures', '.jpg')
    handler.get_all_hash()
    handler.print_all()


if __name__ == "__main__":
    main()
