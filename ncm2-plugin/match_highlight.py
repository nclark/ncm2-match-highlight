# -*- coding: utf-8 -*-

def wrap():
    from ncm2_core import ncm2_core
    from ncm2 import getLogger
    import vim

    index_map = {
            'bold': 1,
            'sans-serif': 2,
            'sans-serif-bold': 3,
            'mono-space': 4,
            'double-struck': 5
            }

    replace_map = [('A', '𝐀', '𝖠', '𝗔', '𝙰', '𝔸'),
                   ('B', '𝐁', '𝖡', '𝗕', '𝙱', '𝔹'),
                   ('C', '𝐂', '𝖢', '𝗖', '𝙲', 'ℂ'),
                   ('D', '𝐃', '𝖣', '𝗗', '𝙳', '𝔻'),
                   ('E', '𝐄', '𝖤', '𝗘', '𝙴', '𝔼'),
                   ('F', '𝐅', '𝖥', '𝗙', '𝙵', '𝔽'),
                   ('G', '𝐆', '𝖦', '𝗚', '𝙶', '𝔾'),
                   ('H', '𝐇', '𝖧', '𝗛', '𝙷', 'ℍ'),
                   ('I', '𝐈', '𝖨', '𝗜', '𝙸', '𝕀'),
                   ('J', '𝐉', '𝖩', '𝗝', '𝙹', '𝕁'),
                   ('K', '𝐊', '𝖪', '𝗞', '𝙺', '𝕂'),
                   ('L', '𝐋', '𝖫', '𝗟', '𝙻', '𝕃'),
                   ('M', '𝐌', '𝖬', '𝗠', '𝙼', '𝕄'),
                   ('N', '𝐍', '𝖭', '𝗡', '𝙽', 'ℕ'),
                   ('O', '𝐎', '𝖮', '𝗢', '𝙾', '𝕆'),
                   ('P', '𝐏', '𝖯', '𝗣', '𝙿', 'ℙ'),
                   ('Q', '𝐐', '𝖰', '𝗤', '𝚀', 'ℚ'),
                   ('R', '𝐑', '𝖱', '𝗥', '𝚁', 'ℝ'),
                   ('S', '𝐒', '𝖲', '𝗦', '𝚂', '𝕊'),
                   ('T', '𝐓', '𝖳', '𝗧', '𝚃', '𝕋'),
                   ('U', '𝐔', '𝖴', '𝗨', '𝚄', '𝕌'),
                   ('V', '𝐕', '𝖵', '𝗩', '𝚅', '𝕍'),
                   ('W', '𝐖', '𝖶', '𝗪', '𝚆', '𝕎'),
                   ('X', '𝐗', '𝖷', '𝗫', '𝚇', '𝕏'),
                   ('Y', '𝐘', '𝖸', '𝗬', '𝚈', '𝕐'),
                   ('Z', '𝐙', '𝖹', '𝗭', '𝚉', 'ℤ'),
                   ('a', '𝐚', '𝖺', '𝗮', '𝚊', '𝕒'),
                   ('b', '𝐛', '𝖻', '𝗯', '𝚋', '𝕓'),
                   ('c', '𝐜', '𝖼', '𝗰', '𝚌', '𝕔'),
                   ('d', '𝐝', '𝖽', '𝗱', '𝚍', '𝕕'),
                   ('e', '𝐞', '𝖾', '𝗲', '𝚎', '𝕖'),
                   ('f', '𝐟', '𝖿', '𝗳', '𝚏', '𝕗'),
                   ('g', '𝐠', '𝗀', '𝗴', '𝚐', '𝕘'),
                   ('h', '𝐡', '𝗁', '𝗵', '𝚑', '𝕙'),
                   ('i', '𝐢', '𝗂', '𝗶', '𝚒', '𝕚'),
                   ('j', '𝐣', '𝗃', '𝗷', '𝚓', '𝕛'),
                   ('k', '𝐤', '𝗄', '𝗸', '𝚔', '𝕜'),
                   ('l', '𝐥', '𝗅', '𝗹', '𝚕', '𝕝'),
                   ('m', '𝐦', '𝗆', '𝗺', '𝚖', '𝕞'),
                   ('n', '𝐧', '𝗇', '𝗻', '𝚗', '𝕟'),
                   ('o', '𝐨', '𝗈', '𝗼', '𝚘', '𝕠'),
                   ('p', '𝐩', '𝗉', '𝗽', '𝚙', '𝕡'),
                   ('q', '𝐪', '𝗊', '𝗾', '𝚚', '𝕢'),
                   ('r', '𝐫', '𝗋', '𝗿', '𝚛', '𝕣'),
                   ('s', '𝐬', '𝗌', '𝘀', '𝚜', '𝕤'),
                   ('t', '𝐭', '𝗍', '𝘁', '𝚝', '𝕥'),
                   ('u', '𝐮', '𝗎', '𝘂', '𝚞', '𝕦'),
                   ('v', '𝐯', '𝗏', '𝘃', '𝚟', '𝕧'),
                   ('w', '𝐰', '𝗐', '𝘄', '𝚠', '𝕨'),
                   ('x', '𝐱', '𝗑', '𝘅', '𝚡', '𝕩'),
                   ('y', '𝐲', '𝗒', '𝘆', '𝚢', '𝕪'),
                   ('z', '𝐳', '𝗓', '𝘇', '𝚣', '𝕫'),
                   ('0', '𝟎', '𝟢', '𝟬', '𝟶', '𝟘'),
                   ('1', '𝟏', '𝟣', '𝟭', '𝟷', '𝟙'),
                   ('2', '𝟐', '𝟤', '𝟮', '𝟸', '𝟚'),
                   ('3', '𝟑', '𝟥', '𝟯', '𝟹', '𝟛'),
                   ('4', '𝟒', '𝟦', '𝟰', '𝟺', '𝟜'),
                   ('5', '𝟓', '𝟧', '𝟱', '𝟻', '𝟝'),
                   ('6', '𝟔', '𝟨', '𝟲', '𝟼', '𝟞'),
                   ('7', '𝟕', '𝟩', '𝟳', '𝟽', '𝟟'),
                   ('8', '𝟖', '𝟪', '𝟴', '𝟾', '𝟠'),
                   ('9', '𝟗', '𝟫', '𝟵', '𝟿', '𝟡'), ]

    old_matches_filter = ncm2_core.matches_filter

    def new_matches_filter(*args):
        data = args[0]
        matches = args[-1]
        matches = old_matches_filter(*args)
        idx = index_map[data['match_highlight']]

        for m in matches:
            ud = m['user_data']
            key = ud.get('match_key', 'abbr')
            hl = ud.get('match_highlight', [])
            if key == 'word':
                continue
            for b, e in hl:
                sub = m[key][b:e]
                for rp in replace_map:
                    sub = sub.replace(rp[0], rp[idx])
                a = m[key]

                # somehow the last highligted character is not properly
                # displayed in the terminal, append a space as workaround
                m[key] = a[:b] + sub + (a[e:] or ' ')

        return matches

    ncm2_core.matches_filter = new_matches_filter

    vim.command(r'''
        let g:ncm2#match_highlight = get(g:, "ncm2#match_highlight", "double-struck")
        call ncm2#hook_coredata(1, ['complete', 'on_complete'], 'match_highlight', {d -> extend(d, {'match_highlight': g:ncm2#match_highlight}, "force")})
    ''')


wrap()
