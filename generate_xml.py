#!/usr/bin/env python3


WALLPAPERS = {
    "Paii Lineage": {
        "author": "Paii",
        "featured": "paii_lineage_04",
        "wallpapers": {
            "Lineage": {
                "1": "01",
                "2": "02",
                "3": "03",
                "4": "04",
                "5": "05",
                "6": "06",
                "7": "07",
                "8": "08",
                "9": "09",
            },
        },
    },
}

WALLPAPERS_XML_HEADER = """<?xml version="1.0" encoding="utf-8" ?>
<!--
    Copyright (C) 2024 The AtigaOS Project

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
-->
<wallpapers>"""

WALLPAPERS_XML_FOOTER = """

</wallpapers>
"""

STRINGS_XML_HEADER = """<?xml version="1.0" encoding="utf-8"?>
<!--
    Copyright (C) 2024 The Atiga Project

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
-->
<resources>"""

STRINGS_XML_FOOTER = """
</resources>
"""

strings = {}

with open("res/xml/wallpapers.xml", "w+") as f:
    f.write(WALLPAPERS_XML_HEADER)

    for category_name, cat_info in WALLPAPERS.items():
        category_id = category_name.lower().replace(" ", "_")
        strings[f"category_{category_id}"] = category_name

        author = cat_info["author"]
        author_id = author.lower().replace(" ", "_")
        strings[f"author_{author_id}"] = f"by {author}"

        f.write(f"""

    <category id="{category_id}" title="@string/category_{category_id}" featured="{cat_info['featured']}">""")

        for set_name, wallpapers in cat_info["wallpapers"].items():
            set_id = set_name.lower().replace(" ", "_")

            for wp_id, wp_name in sorted(wallpapers.items(), key=lambda w: w[1]):
                wp_res_id = f"{category_id}_{set_id}_{wp_id}"
                strings[f"wallpaper_{wp_res_id}"] = f"{set_name} \u2022 {wp_name}"

                f.write(f"""

        <static-wallpaper
            id="{wp_res_id}"
            src="@drawable/{wp_res_id}"
            title="@string/wallpaper_{wp_res_id}"
            subtitle1="@string/author_{author_id}" />""")

        f.write("""

    </category>""")

    f.write(WALLPAPERS_XML_FOOTER)

with open("res/values/wallpaper_strings.xml", "w+") as f:
    f.write(STRINGS_XML_HEADER)

    for str_id, value in strings.items():
        f.write(f"""
    <string name="{str_id}">{value}</string>""")

    f.write(STRINGS_XML_FOOTER)
