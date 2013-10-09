{
  "targets": [ {
      "target_name": "nfc",
          "sources": [ "src/nfc.cc" ],
          'conditions': [
          		['OS=="linux"',
          			{
          				"link_settings": {
           			    	"libraries": [ "-lnfc" ]
          				}
          			}
          		],
          		['OS=="mac"',
          			{
            			'defines': [
              				'__MACOSX_CORE__'
            			],
          				'include_dirs': [
            				'/opt/local/include',
          				],
          				'libraries': [
            				'-L/opt/local/lib'
          				]
           			}

          		]
           ]
       }
    ]
}
