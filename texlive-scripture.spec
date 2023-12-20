Name:		texlive-scripture
Version:	65493
Release:	1
Summary:	A LaTeX style for typesetting Bible quotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scripture
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scripture.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scripture.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scripture.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The scripture package provides a set of macros for typesetting
quotations from the Bible. It provides many features commonly
seen in Bibles such as dropped text for chapter numbers,
superscripts for verse numbers, indented lines for poetry
sections, narrow sections and hanging paragraphs. A reference
for the quotation can optionally be added.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/scripture
%{_texmfdistdir}/tex/latex/scripture
%doc %{_texmfdistdir}/doc/latex/scripture

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
